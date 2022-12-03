# Author: Lesley Miller
# Date: Dec 2, 2022
import pandas as pd

def get_shape_score(play):
    """
    Return the score based on which shape was played be it rock, paper or scissors.
    Scores are as follows:
    Rock = 1
    Paper = 2
    Scissors = 3

    Parameters
    ----------
    play (str) A string of either X, Y or Z where X = Rock, Y = Paper and Z = scissors
    Returns
    -------
    int
        The score of the round based on whether rock, paper or scissor was used

    """
    if play == "X":
        return 1
    elif play == "Y":
        return 2
    else:
        return 3

def get_player2_outcome_score(player1, player2):
    """
    Returns the score of player2 for the round based on the outcome (loss, draw, win).
    Scores are as follows:
    loss = 0
    draw = 3
    win = 6

    Parameters
    ----------
    player1 (str) A string of either A, B or C
    player2 (str) A string of either X, Y or Z

    Returns
    -------
    int
        The score of the outcome for player2.

    """
    # if player1 plays a Rock
    if player1 == "A":
        # player2 plays Rock and there's a draw
        if player2 == "X":
            return 3
        # player2 plays Paper and wins
        elif player2 == "Y":
            return 6
        # player2 plays scissors and loses
        else:
            return 0
    # player1 plays Paper
    elif player1 == "B":
        # player2 plays rock and loses
        if player2 == "X":
            return 0
        # player2 plays Paper and there's a draw
        elif player2 == "Y":
            return 3
        # player2 has played scissors and wins
        else:
            return 6

    # player1 plays scissors
    else:
        # player 2 plays Rock and wins
        if player2 == "X":
            return 6
        # player2 plays Paper and loses
        elif player2 == "Y":
            return 0
        # player2 plays scissors and there's a draw
        else:
            return 3

def convert_outcome_code(outcome_code):
    """
    Convert outcome code to the outcome description.

    Parameters
    ----------
    outcome_code (str) One of X = lose, Y = draw, Z = win

    Returns
    -------
    str
        A string of either lose, draw or win.

    """
    if outcome_code == "X":
        return "lose"
    elif outcome_code == "Y":
        return "draw"
    else:
        return "win"


def determine_shape2play(player1, outcome):
    """
    Determine which shape to play for player2 based on what player1 has played
    and what the outcome is supposed to be.

    Parameters
    ----------
    player1 (str) One of A, B or C where A = Rock, B = Paper and C = Scissors
    outcome (str) One of "lose", "draw" or "win"
    Returns
    -------
    str
        The shape to play of either X = Rock, Y = Paper or Z = Scissors

    """
    if outcome == "draw":
        # play the same shape as player1
        if player1 == "A":
            return "X"
        elif player1 == "B":
            return "Y"
        else:
            return "Z"
    elif outcome == "lose":
        if player1 == "A":
            return "Z"
        elif player1 == "B":
            return "X"
        else:
            return "Y"
    else:
        if player1 == "A":
            return "Y"
        elif player1 == "B":
            return "Z"
        else:
            return "X"



def main():
    # import the data
    strat_guide = pd.read_csv("input.txt", sep=' ', names=["player1", "outcome"])
    # convert the outcome code to outcome description
    strat_guide['outcome'] = strat_guide.outcome.apply(convert_outcome_code)

    # determine which shape to play for player2
    strat_guide["player2"] = strat_guide.player1.combine(strat_guide.outcome, func=determine_shape2play)

    # add shape score for each round to the df
    strat_guide["player2_shape_score"] = strat_guide.player2.apply(get_shape_score)
    # add outcome score for each round to the df
    strat_guide["player2_outcome_score"] = strat_guide.player1.combine(strat_guide.player2, func=get_player2_outcome_score)
    # calculate player2 total score
    strat_guide["player2_total_score"] = strat_guide.player2_shape_score + strat_guide.player2_outcome_score

    # return player2 total score from all rounds
    print("My score is: " + str(strat_guide.player2_total_score.sum()))


if __name__ == '__main__':
    main()