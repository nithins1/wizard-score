from collections import defaultdict
import os

has_termcolor = True
try:
    from termcolor import colored
except ImportError:
    has_termcolor = False

def input_int(prompt, max_val=-1):
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
        if in_str.isnumeric() and max_val != -1 and int(in_str) <= max_val:
            return int(in_str)
        else:
            if has_termcolor:
                prompt = colored(prompt, "red", attrs=['bold'])

if __name__ == "__main__":
    CORRECT_BASE_POINTS = 20
    PER_WIN_POINTS = 10

    names = input("Enter names (sep. by spaces): ").split()

    width, height = os.get_terminal_size()
    total_cards = len(names) # Total number of cards involved in the current round
    round_num = 1 # Current round number
    cell_size = len(max(names, key=len)) + 2# Number of characters in each cell in table
    cell_size = cell_size + 1 if cell_size % 2 == 1 else cell_size
    if cell_size < 6:
        cell_size = 6
    score = defaultdict(int) # Current score for each player

    table = "" # Contains entire game history as string
    for n in names:
        table += "|" + n.center(cell_size)
    table += "|\n"
    row_break = '-' * (len(table) - 1) + "\n" # Dashed line to break up table
    table += row_break
    #print(table)
    while total_cards < 60:
        print(f"ROUND {round_num}".center(width, '-'))

        bids = {}
        wins = {}
        for n in names:
            bids[n] = input_int(f"{n} bid: ", round_num)

        for n in names:
            wins[n] = input_int(f"{n} wins: ", round_num)

        # Print bid followed by wins for each player
        for n in names:
            table += "|" + str(bids[n]).center(cell_size // 2) + str(wins[n]).center(cell_size // 2)
        table += "|\n"

        for n in names:
            if bids[n] == wins[n]:
                score[n] += CORRECT_BASE_POINTS + wins[n] * PER_WIN_POINTS
            else:
                score[n] -= abs(wins[n] - bids[n]) * PER_WIN_POINTS
            table += "|" + str(score[n]).center(cell_size)
        table += "|\n"
        table = row_break + table + row_break
        print(table)
        round_num += 1
        total_cards += len(names)
