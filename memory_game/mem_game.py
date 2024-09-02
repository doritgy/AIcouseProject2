import random
import time
import os
import subprocess

game_data = {
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'game_over': False,
        'board': {},
        'move_history': []  # all of the card flips till now: I don't need this for my game
    }

def init_game() -> dict[any]:
    """
    Initializes the game data structure.
    go to prepare board and back
    Returns:
        dict: A dictionary containing game settings, including the number of rows and columns,
              player scores, the game board, and other necessary game state information.
    """
    rows, columns = 4, 4
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']

    global game_data
    game_data = {
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'game_over': False,
        'board': prepare_board(rows, columns, cards),
        'move_history': []  # all of the card flips till now
    }
    return game_data


def prepare_board(rows:int, columns:int, cards:list[str]) -> dict[any]:
    """
    Prepares the game board by shuffling cards and placing them into the board structure.

    Args:
        rows (int): Number of rows in the board.
        columns (int): Number of columns in the board.
        cards (list): List of card values to be placed on the board.

    Returns:
        dict: A dictionary representing the game board, where each key is a tuple (row, col)
              and the value is a dictionary with card information (card value, flipped state, matched state).
    """
    global game_data
    board = {}
    random.shuffle(cards)
    print(cards)
    # place the cards in the board
    for i in range(rows):
        for j in range(columns):
            board[(i, j)] = {'card': cards.pop(), 'flipped': False, 'matched': False}
            #print("board", board[(i, j)])
    # print("cards", cards)
    # print("board", board)
    return board


def play(rows, columns) -> None:
    """
    Runs the main game loop, handling player turns, guessing, and score updates.

    Args:
        game_data is a global variable, so every function can change it
    """
    global game_data
    while True:
        (ret_guess1, ret_guess2) = get_guesses()
        guess1, guess2 = (ret_guess1, ret_guess2)
        game_data['board'][guess1]['flipped'] = True
        game_data['board'][guess2]['flipped'] = True
        display_board(rows, columns)
        if game_data['board'][guess1]['card'] == game_data['board'][guess2]['card']:
            game_data['board'][guess1]['flipped'] = True
            game_data['board'][guess2]['flipped'] = True
            game_data['board'][guess1]['matched'] = True
            game_data['board'][guess2]['matched'] = True
            if game_data['turn'] == 'player1':
                game_data['score']['player1'] += 1
            else:
                game_data['score']['player2'] += 1
            if check_end(rows, columns):
                if game_data['score']['player1'] > game_data['score']['player2']:
                    print("player 1 you are the winner")
                elif game_data['score']['player1'] == game_data['score']['player2']:
                    print("it's a tye, both were strong")
                else:
                    print("player 2 you are the winner")
                ans = input("another game? y/n")
                if ans == 'y':
                    for i in range(rows):
                        for j in range(columns):
                            game_data['board'][(i, j)]['flipped'] = False
                            game_data['board'][(i, j)]['matched'] = False
                    clear_console()
                    display_board(rows, columns)
                    continue
                else:
                    break
            #continue
        else:
            game_data['board'][guess1]['flipped'] = False
            game_data['board'][guess2]['flipped'] = False
            game_data['board'][guess1]['matched'] = False
            game_data['board'][guess2]['matched'] = False
            if game_data['turn'] == 'player1':
                game_data['turn'] = 'player2'
            else:
                if game_data['turn'] == 'player2':
                   game_data['turn'] = 'player1'
            clear_console()
            display_board(rows, columns)
            continue



def get_guesses():
    guess1:tuple[int, int] = (9, 9)
    guess2:tuple[int, int] = (9, 9)

    while True:
        try:
            if game_data['turn'] == 'player1':
                while True:
                    guess1_row = int(input("player 1 please type row  for the first guess"))
                    if guess1_row > rows:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess1_row).isalpha():
                        raise ValueError("the guess is illegal, try again ")

                    break

                while True:
                    guess1_col = int(input("player 1 please type column  for the second guess"))
                    if guess1_col > columns:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess1_col).isalpha():
                        raise ValueError("the guess is illegal, try again ")

                    break

                guess1 = (guess1_row, guess1_col)
            else:
                while True:
                    guess1_row = int(input("player 2 please type row  for the first guess"))
                    if guess1_row > rows:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess1_row).isalpha():
                        raise ValueError("the guess is illegal, try againn")

                    break

                while True:
                    guess1_col = int(input("player 2 please type column  for the second guess"))
                    if guess1_col > columns:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess1_col).isalpha():
                        raise ValueError("the guess is illegal, try again")

                    break
                guess1 = (guess1_row, guess1_col)
            if game_data['board'][guess1]['flipped']:
                raise ValueError("this card is already flipped, try again")
            else:
                game_data['board'][guess1]['flipped'] = True
            if game_data['turn'] == 'player1':
                while True:
                    guess2_row = int(input("player 1 please type row  for the second guess"))
                    if guess2_row > rows:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess2_row).isalpha():
                        raise ValueError("the guess is illegal, try again")

                    break

                while True:
                    guess2_col = int(input("player 1 please type column  for the second guess"))
                    if guess2_col > columns:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess2_col).isalpha():
                        raise ValueError("the guess is illegal, try again ")

                    break

                guess2 = (guess2_row, guess2_col)
                if guess1 == guess2:
                    raise ValueError("you guessed twice the same guess, please try again")
                    continue
                break
            else:
                while True:
                    guess2_row = int(input("player 2 please type row  for the second guess"))
                    if guess2_row > rows:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess2_row).isalpha():
                        raise ValueError("the guess is illegal, try again ")

                    break

                while True:
                    guess2_col = int(input("player 2 please type column  for the second guess"))
                    if guess2_col > columns:
                        raise ValueError("the guess is out of range, please try again")

                    if str(guess2_col).isalpha():
                        raise ValueError("the guess is illegal, try again ")

                    break


                guess2 = (guess2_row, guess2_col)
                if guess1 == guess2:
                    raise ValueError("you guessed twice the same guess,please try again")                                     "")

                if guess1 == (9, 9) or guess2 == (9, 9):
                    continue
                break
        except Exception as e:
            print("the guess is illegal, please try again", str(e))
            continue
    ret_tuple:tuple[tuple, tuple] = (guess1, guess2)
    return ret_tuple



def display_board(rows:int, columns:int) -> None:

    global game_data
    i:int = 0
    j:int = 0
    for i in range(columns):
        for j in range(rows):
            print(game_data['board'][(i, j)]['card'] if game_data['board'][(i, j)]['flipped'] else '*', "  ", end="")
        print()
    print()
    time.sleep(3)

    return None

def check_end(rows, columns) -> bool:
    for i in range(rows):
        for j in range(columns):
            if game_data['board'][(i, j)]['flipped']:
                continue
            else:
                return False
    return True

def clear_console():
    #os.system('cls')
    #subprocess.run("cls", shell=True)
    print("\n" * 100)
    return



"""        
  1 2 3 4
1 * * * A
2 * * * A
3 * * * B
4 * * * B
Player 1, play: 2 2
  1 2 3 4
1 * * * A
2 * C * A
3 * * * B
4 * * * B
Player 1, play: 2 3
  1 2 3 4
1 * * * A
2 * C D A
3 * * * B
4 * * * B
Player 2, play: 
  1 2 3 4
1 * * * A
2 * * * A
3 * * * B
4 * * * B
"""

if __name__ == "__main__":
    rows = 4
    columns = 4
    game_data = init_game()
    play(rows, columns)


