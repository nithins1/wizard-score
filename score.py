from collections import defaultdict
import os
import argparse

try:
    width, height = os.get_terminal_size()
except:
    width, height = 80, 24
has_termcolor = True

# termcolor is recommended but not necessary
try:
    from termcolor import colored
except ImportError:
    has_termcolor = False

def input_int(prompt, max_val=None):
    """
    Gets user input, retrying if the input is not an integer.

        Parameters:
            prompt (string): Prompt printed to console before receiving input
            max_val (int): Optional. Reject all inputs above this value

        Returns:
            (int): integer receieved from user
    """
    while True:
        in_str = input(prompt)
        if in_str.isnumeric() and max_val is not None and int(in_str) <= max_val:
            return int(in_str)
        else: # Retry query but set prompt text to red
            if has_termcolor:
                prompt = colored(prompt, "red", attrs=['bold'])

if __name__ == "__main__":
    LEFT_MARGIN = 12 # Size of left margin for displaying round number in table

    parser = argparse.ArgumentParser(description="Creates score card for a wizard game.")
    parser.add_argument("-v", "--verbose", action="store_true", help="print round number before each row in table")
    parser.add_argument("-n", "--nodisplay", action="store_true", help="only display table at the end of the game")
    parser.add_argument("-b", "--base", type=int, default=10, metavar="<points>", help="base points awarded for bidding correctly")
    parser.add_argument("-p", "--per", type=int, default=10, metavar="<points>", help="points gained/lost per bid")
    parser.add_argument("-c", "--cards", type=int, default=60, metavar="<cards>", help="total cards in game")
    args = parser.parse_args()

    names = input("Enter names (sep. by spaces): ").split()
    if len(names) < 2:
        print("Invalid number of players.")
        exit(1)

    total_cards = len(names) # Total number of cards involved in the current round
    round_num = 1 # Current round number
    cell_size = len(max(names, key=len)) + 2 # Number of characters in each cell in table
    cell_size = cell_size + 1 if cell_size % 2 == 1 else cell_size
    if cell_size < 6:
        cell_size = 6
    score = defaultdict(int) # Current score for each player

    table = "" # Contains entire game history as string

    if args.verbose:
        table += " " * LEFT_MARGIN
    for n in names:
        table += "|" + n.center(cell_size)
    table += "|\n"
    row_break = '-' * (len(table) - 1) + "\n" # Dashed line to break up table
    table = row_break + table + row_break
    while total_cards <= args.cards:
        print(f"ROUND {round_num}".center(width, '-'))

        bids = {} # Bid for each player in the current round
        wins = {} # Number of tricks won in the current round

        # Query for each player's bid number
        for n in names:
            bids[n] = input_int(f"{n}'s bid: ", round_num)

        # Query for each player's win number
        for n in names:
            wins[n] = input_int(f"{n}'s wins: ", round_num)

        if args.verbose:
            table += f"Round {round_num}:".ljust(LEFT_MARGIN)

        # Print bid followed by wins for each player
        for n in names:
            table += "|" + str(bids[n]).center(cell_size // 2) + str(wins[n]).center(cell_size // 2)
        table += "|\n"

        if args.verbose:
            table += " " * LEFT_MARGIN

        # Compute current score for every player
        for n in names:
            # Bid was correct
            if bids[n] == wins[n]:
                score[n] += args.base + wins[n] * args.per

            # Bid was incorrect
            else:
                score[n] -= abs(wins[n] - bids[n]) * args.per

            # Add scores to table
            table += "|" + str(score[n]).center(cell_size)

        table += "|\n"
        table += row_break
        if not args.nodisplay:
            print(table)
        round_num += 1
        total_cards += len(names)

    # Print final state of board
    if args.nodisplay:
        print(table)
    exit(0)
