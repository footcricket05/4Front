#!/usr/bin/env python
# coding: utf-8

# In[13]:


import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.geometry("950x640")
root.configure(background="#b8d0eb")
root.resizable(False, False)
tk.Wm.wm_title(root, "4Front")
l1, l2, l3, l4, l5, l6, l7, turns, piece = [0]*9

# Scores
red_score = 0
yellow_score = 0

# Game board
tk.Label(root, bg="#004e98", width=80, height=32, bd=5, relief="solid").place(x=60,y=30)

# Turn Label
tk.Label(root, text="TURN: ", font=("Courier", 40, "bold"), bg="#b8d0eb").place(x=660,y=250)

# Turn color indicator
class TurnIndicator:
    def __init__(self, root):
        self._turn = tk.Label(root, bg="#e74545", width=6, height=3, bd=2, relief="solid")
turn_color = TurnIndicator(root)
turn_color._turn.place(x=850,y=257)

# Reset function
def reset_c():
    global l1, l2, l3, l4, l5, l6, l7, turns
    l1, l2, l3, l4, l5, l6, l7, turns = [0]*8
    for row in [a, b, c, d, e, f]:
        for box in row:
            box.a.configure(bg="#004e98")

# Reset Button
tk.Button(root, text="RESET", font=("Courier", 30, "bold"), bg="#e74545", bd=4, relief="solid", command=reset_c).place(x=725,y=480)

# Function to change colors
def colors():
    global turns
    if turns % 2 == 0:
        turn_color._turn.configure(bg="#faf968")
        return "#e74545"
    else: 
        turn_color._turn.configure(bg="#e74545")
        return "#faf968"

# Box class
class Box:
    def __init__(self, root):
        self.a = tk.Label(root, bg="#004e98", width=8, height=4, bd=2, relief="solid")

# Button class
class Button:
    def __init__(self, root, value):
        self.butt = tk.Button(root, bg="#26cca3", text=str(value), font=("Courier",22,"bold"), width=3, height=1, bd="3", relief="solid", command=lambda: pos(value))

# Boxes
a = [Box(root) for _ in range(7)]
b = [Box(root) for _ in range(7)]
c = [Box(root) for _ in range(7)]
d = [Box(root) for _ in range(7)]
e = [Box(root) for _ in range(7)]
f = [Box(root) for _ in range(7)]
rows = [a, b, c, d, e, f]

# Place boxes
for i, row in enumerate(rows):
    for j, box in enumerate(row):
        box.a.place(x=75 + 80*j, y=45 + 80*i)

# Buttons
buttons = [Button(root, i+1) for i in range(7)]
for i, button in enumerate(buttons):
    button.butt.place(x=75 + 80*i, y=530)

# Function to handle button positions
# Function to handle button positions
def pos(value):
    global l1, l2, l3, l4, l5, l6, l7, turns

    if value == 1:
        if l1 < 6:
            rows[5 - l1][0].a.config(bg=colors())
            l1 += 1

    elif value == 2:
        if l2 < 6:
            rows[5 - l2][1].a.config(bg=colors())
            l2 += 1

    elif value == 3:
        if l3 < 6:
            rows[5 - l3][2].a.config(bg=colors())
            l3 += 1

    elif value == 4:
        if l4 < 6:
            rows[5 - l4][3].a.config(bg=colors())
            l4 += 1

    elif value == 5:
        if l5 < 6:
            rows[5 - l5][4].a.config(bg=colors())
            l5 += 1

    elif value == 6:
        if l6 < 6:
            rows[5 - l6][5].a.config(bg=colors())
            l6 += 1

    elif value == 7:
        if l7 < 6:
            rows[5 - l7][6].a.config(bg=colors())
            l7 += 1

    if check_four_in_a_row():
        winner = "Red" if turns % 2 == 0 else "Yellow"
        display_winner_and_reset(winner)
    else:
        turns += 1

# Check for four in a row
def check_four_in_a_row():
    # Check horizontal
    for row in rows:
        for i in range(4):
            if row[i].a['bg'] == row[i+1].a['bg'] == row[i+2].a['bg'] == row[i+3].a['bg'] != "#004e98":
                return True

    # Check vertical
    for col in range(7):
        for i in range(3):
            if rows[i][col].a['bg'] == rows[i+1][col].a['bg'] == rows[i+2][col].a['bg'] == rows[i+3][col].a['bg'] != "#004e98":
                return True

    # Check diagonal (down-right and up-right)
    for i in range(3):
        for j in range(4):
            if rows[i][j].a['bg'] == rows[i+1][j+1].a['bg'] == rows[i+2][j+2].a['bg'] == rows[i+3][j+3].a['bg'] != "#004e98":
                return True
            if rows[i+3][j].a['bg'] == rows[i+2][j+1].a['bg'] == rows[i+1][j+2].a['bg'] == rows[i][j+3].a['bg'] != "#004e98":
                return True

    return False

# Display winner and reset game
def display_winner_and_reset(winner):
    global red_score, yellow_score

    if winner == "Red":
        red_score += 1
    elif winner == "Yellow":
        yellow_score += 1

    tkinter.messagebox.showinfo("Game Over", f"{winner} wins!\nScores:\nRed: {red_score}\nYellow: {yellow_score}")
    reset_c()

root.bind("<Key>", lambda event: pos(int(event.char) if event.char.isdigit() else None))
root.mainloop()


# In[ ]:




