
import tkinter as tk
import random
import time

# Initialize the main window
root = tk.Tk()
root.title("Memory Game")

# Game configuration
rows, cols = 4, 4  # Grid size (4x4)
cards = list('AABBCCDDEEFFGGHH')  # Pairs of letters for matching
random.shuffle(cards)  # Shuffle cards

# Game state variables
buttons = {}  # Store button widgets
first_card = None
second_card = None
matches_found = 0

# Game functions
def on_button_click(row, col):
    global first_card, second_card, matches_found

    button = buttons[(row, col)]

    if button["text"] != "":  # Ignore already flipped cards
        return

    card_text = card_values[(row, col)]
    button.config(text=card_text, state="disabled")  # Reveal card

    if first_card is None:
        first_card = (row, col)
    else:
        second_card = (row, col)

        # Compare cards after a short delay
        root.after(500, check_for_match)

def check_for_match():
    global first_card, second_card, matches_found

    row1, col1 = first_card
    row2, col2 = second_card

    if card_values[(row1, col1)] == card_values[(row2, col2)]:
        buttons[(row1, col1)].config(bg="green")
        buttons[(row2, col2)].config(bg="green")
        matches_found += 1
    else:
        buttons[(row1, col1)].config(text="", state="normal")
        buttons[(row2, col2)].config(text="", state="normal")

    first_card, second_card = None, None

    if matches_found == len(cards) // 2:
        print("Congratulations! You've matched all pairs!")

# Prepare the grid of buttons
card_values = {}
for i in range(rows):
    for j in range(cols):
        card_values[(i, j)] = cards.pop()

        button = tk.Button(root, text="", width=8, height=4,
                           command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j)

        buttons[(i, j)] = button

# Start the game loop
root.mainloop()