# wizard-score

### What it does:
- Generates scorecard for a game of wizard
- Receives command-line input from user each round

### Example:
First enter the names of the players. Then, each round, do the following:
- During the bidding phase, enter each player's bid.
- After the round is complete, enter the number of tricks each player won

![Example score sheet for round 1](https://images2.imgbox.com/1f/3b/4Tg6hNZK_o.png)
After each round, the results table is printed. The upper two numbers in each box are the player's bid and actual number of tricks won, and the lower number is the player's current score. This format is similar to a traditional [paper-and-pencil scorecard](https://www.usgamesinc.com/images/wizard_score_sheet.pdf).

All user inputs during the game must be integers. If the program encounters an input that is not an integer or is invalid (e.g. bidding 4 when there are only 3 cards) it retries the query.
![Example score sheet for round 1](https://images2.imgbox.com/6f/34/3MtfuwNr_o.png)

### Installation:
- Install [Python 3](https://www.python.org/)
- [Optional] Install dependencies (`pip install -r requirements.txt`)

### How to run:
Run with defaults (recommended): `python score.py`

Optional arguments:
![Arguments Explanation](https://images2.imgbox.com/c3/13/x6r32QRA_o.png)
