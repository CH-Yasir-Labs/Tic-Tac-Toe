#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     03/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"]== buttons[combo[1]]["text"]== buttons[combo[2]]["text"]!="":

            for i in combo:
               buttons[i].config(bg="green")
            winner = True

            messagebox.showinfo("Tic-Tac-Toe",f"Player {buttons[combo[0]]['text']} wins!")
            update_score(buttons[combo[0]]["text"])
            return

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        winner = True
        return

def button_click(index):
    global winner,current_player
    if buttons[index]["text"]=="" and  not winner:
       buttons[index]["text"]= current_player
       check_winner()
       toggle_player()


def toggle_player():
    global current_player
    current_player= "X" if current_player =="O" else "O"
    label.config(text=f"Player {current_player}'s turn")
    update_turn_indicator()

def update_turn_indicator():
    """Update the label to show whose turn it is."""
    label.config(text=f"Player {current_player}'s turn")
    # Highlight the current player's turn with a different color
    if current_player == "X":
        label.config(fg="blue")
    else:
        label.config(fg="red")

def update_score(winner_player):
    """Update the score based on the winner."""
    global score_X, score_O
    if winner_player == "X":
        score_X += 1
    elif winner_player == "O":
        score_O += 1
    score_label.config(text=f"Score - X: {score_X} | O: {score_O}")



def restart_game():
    """Resets the game board for a new match."""
    global current_player, winner
    winner = False
    current_player = "X"

    # Reset all buttons
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

    update_turn_indicator()

    # Reset label
    label.config(text=f"Player {current_player}'s turn")



root = tk.Tk()
root.title("Tic-Tac-Toe")
buttons=[tk.Button(root,text="",font=("Times New Roman",25),width=6, height=2, command=lambda i=i: button_click(i))for i in range(9)]

for i,button in enumerate(buttons):
    button.grid(row=i //3 ,column =i % 3)

current_player="X"
winner=False
score_X = 0  # Score for player X
score_O = 0  # Score for player O

label=tk.Label(root,text=f"Player {current_player}'s turn",font=("Times New Roman",16))
label.grid(row=3 , column=0 ,columnspan=3)

score_label = tk.Label(root, text=f"Score - X: {score_X} | O: {score_O}", font=("Times New Roman", 14))
score_label.grid(row=5, column=0, columnspan=3)

restart_button = tk.Button(root, text="Restart Game", font=("Times New Roman", 14), command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3)


update_turn_indicator()
root.mainloop()


