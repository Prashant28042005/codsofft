# Task 4
# Name : Prashant Yadav
# Domain : Python

# User Input: Prompt the user to choose rock, paper, or scissors.
# Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
# Game Logic: Determine the winner based on the user's choice and the computer's choice.
# Rock beats scissors, scissors beat paper, and paper beats rock.
# Display Result: Show the user's choice and the computer's choice.
# Display the result, whether the user wins, loses, or it's a tie.
# Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
# Play Again: Ask the user if they want to play another round.
# User Interface: Design a user-friendly interface with clear instructions and feedback.


import tkinter as tk
from tkinter import messagebox
import random

# Game logic functions
def get_computer_choice():
    return random.choice(options)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game(player_choice):
    global player_score, computer_score

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    if result == "tie":
        result_message = "It's a tie!"
    elif result == "win":
        result_message = "You win!"
        player_score += 1
    else:
        result_message = "You lose!"
        computer_score += 1

    # Update the result and score labels
    result_label.config(text=f"Player chose: {player_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}\n{result_message}")
    score_label.config(text=f"Score - Player: {player_score} | Computer: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Define options and scores
options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0

# Create and place widgets
root.configure(bg='#f0f0f0')  # Light grey background

# Title label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), bg='#f0f0f0')
title_label.pack(pady=20)

intro_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14), bg='#f0f0f0')
intro_label.pack(pady=10)

# Create a frame for buttons
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 12), width=10, height=2, command=lambda: play_game("rock"), bg='#d3d3d3')
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 12), width=10, height=2, command=lambda: play_game("paper"), bg='#d3d3d3')
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 12), width=10, height=2, command=lambda: play_game("scissors"), bg='#d3d3d3')
scissors_button.grid(row=0, column=2, padx=10)

# Result and score labels
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg='#f0f0f0')
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - Player: 0 | Computer: 0", font=("Helvetica", 14, "bold"), bg='#f0f0f0')
score_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
