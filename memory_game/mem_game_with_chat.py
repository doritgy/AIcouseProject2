import random
import time
import tkinter as tk

game_data = {
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'game_over': False,
        'board': {},
        'move_history': []  # all of the card flips till now
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
    random.shuffle(cards)
    i:int = 0
    j:int = 0


    global game_data
    global buttons
    game_data = {
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'game_over': False,
        'board': prepare_board(rows, columns, cards),
        'move_history': []} # all of the card flips till now
    print("we are here", game_data['board'])

    root = tk.Tk()
    root.mainloop()
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
    global buttons
    #print(cards)
    # place the cards in the board- i.e.
    buttons = {}
    root = tk.Tk()
    root.title("Memory Game")

    for i in range(rows):
        for j in range(columns):
            board[(i, j)] = {'card': cards[i * (rows - 1) + j], 'flipped': False, 'matched': False}
            button = tk.Button(root, text="", width=8, height=4,
                               command=lambda i=i, j=j: get_guesses(i, j))
            button.grid(row=i, column=j)
            buttons[(i, j)] = button
            #print("board", board[(i, j)])
    #print("cards", cards)
    #print("board", board)

    return board


def play(rows:int, columns:int, ret_tuple:tuple[tuple, tuple]) -> None:
    """
    Runs the main game loop, handling player turns, guessing, and score updates.

    Args:
        game_data is a global variable, so every function can change it
    """

    global game_data
    global buttons
    while True:

        guess1, guess2 = ret_tuple
        print(guess1)
        print(guess2)

        game_data['board'][guess1]['flipped'] = True
        game_data['board'][guess2]['flipped'] = True
        #display_board(rows, columns)
        if game_data['board'][guess1]['card'] == game_data['board'][guess2]['card']:
            game_data['board'][guess1]['card']['flipped'] = True
            game_data['board'][guess2]['card']['flipped'] = True
            game_data['board'][guess1]['card']['matched'] = True
            game_data['board'][guess2]['card']['matched'] = True
            if game_data['turn'] == 'player1':
                game_data['score']['player1'] += 1
            else:
                game_data['score']['player2'] += 1
            continue
        else:
            game_data['board'][guess1]['flipped'] = False
            game_data['board'][guess2]['flipped'] = False
            game_data['board'][guess1]['matched'] = False
            game_data['board'][guess2]['matched'] = False
            if game_data['turn'] == 'player1':
                game_data['turn'] = 'player2'
            else:
                if game_data['turn'] == 'player2':
                   game_data['turn'] == 'player1'
            #display_board(rows, columns)
            if check_end(rows, columns):
                if game_data['score']['player1'] > game_data['score']['player2']:
                    print("player 1 you are the winner")
                elif  game_data['score']['player1'] == game_data['score']['player2']:
                    print("it's a tye, both were strong")
                else:
                    print("player 2 you are the winner")
                ans = input("another game? y/n")
                if ans == 'y':
                    continue
                else:
                    break
            else:
                continue


def get_guesses(i, j):
    guess1:tuple[int, int] = (9, 9)
    guess2:tuple[int, int] = (9, 9)

    try:
        if guess1 == (9, 9):
            guess1 = (i, j)
            print(guess1)
            print(game_data['board'][guess1]['flipped'])
            if game_data['board'][guess1]['flipped']:
                raise ValueError("this card is already flipped, try again")
            else:
                game_data['board'][guess1]['flipped'] = True
        else:
            guess2 = (i, j)
            if game_data['board'][guess2]['flipped']:
                raise ValueError("this card is already flipped, try again")
            else:
                game_data['board'][guess2]['flipped'] = True
        if guess1 == guess2:
            raise ValueError("you guessed twice the same guess, try again")

    except Exception as e:
        print("the guess is illegal, please try again", str(Exception(e)))
    if guess1 != (9, 9) and guess2 != (9, 9):
        ret_tuple:tuple[tuple, tuple] = (guess1, guess2)
        play(rows, columns, ret_tuple)



def display_board(rows:int, columns:int) -> None:
    global game_data
    global buttons
    i:int = 0
    j:int = 0
    for i in range(columns):
        for j in range(rows):
            button = buttons[i, j]
            if game_data['board']['flipped']:
                button.config(text = game_data["board"][i, j]['card'], state="disabled")  # Reveal card
            #print(game_data['board'][(i, j)]['card'] if game_data['board'][(i, j)]['flipped'] else '*', "  ", end = "")
        #print()
    #print()
    time.sleep(3)
    return None

def check_end(rows, columns) -> bool:
    for i in range(rows):
        for j in range(columns):
            if game_data['board'][(i, j)]['matched']:
                continue
            else:
                return False
    return True


if __name__ == "__main__":
    rows = 4
    columns = 4
    game_data = init_game()
    #prepare_board(rows, columns, cards)
    print(game_data)
    print(game_data['board'])
    #play(rows, columns)