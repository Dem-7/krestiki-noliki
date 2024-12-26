
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

current_player = "X"
buttons = []
player_scores = {"X": 0, "O": 0}
max_wins = 3

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        player_scores[current_player] += 1
        update_score()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_game()
    elif check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"

def reset_game():
    for row in buttons:
        for btn in row:
            btn["text"] = ""
    global current_player
    current_player = "X"  # Сначала всегда крестик

def update_score():
    score_label.config(text=f"Счет: X {player_scores['X']} - O {player_scores['O']}")
    if player_scores[current_player] >= max_wins:
        messagebox.showinfo("Игра завершена", f"Игрок {current_player} выиграл {max_wins} раз(а)!")
        reset_scores()

def reset_scores():
    player_scores["X"] = 0
    player_scores["O"] = 0
    update_score()

# Создание интерфейса
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

score_label = tk.Label(window, text="Счет: X 0 - O 0", font=("Arial", 14))
score_label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(window


, text="Сбросить игру", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

window.mainloop()
