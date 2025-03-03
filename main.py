import tkinter
import random
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Calibri", 40, "normal")
SCORE = 0
dict_list = {}
word_list = []

# MAIN WINDOW
root = tkinter.Tk()
root.title("Flash Card App")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

with open("data/french_words.csv", "r") as data:
    for key in data:
        word = key.split(",")
        dict_list[word[0]] = word[1]

for key in dict_list:
    word_list.append(key)


def incorrect():
    title = new_card()
    reveal_answer(title)


def correct():
    title = new_card()
    reveal_answer(title)


def new_card():
    title = random.choice(word_list)
    card_front.delete("title")
    card_front.delete("word")
    card_front.create_text(400, 150, text=f"{title}", font=FONT, tags="title")
    return title


def reveal_answer(title):
    global word
    word = dict_list[title]
    card_front.after(2000, card_front_create_word)


def card_front_create_word():
    card_front.create_text(400, 263, text=f"{word}", font=FONT, tags="word")


# WIDGETS INSIDE CANVAS
card_front_img = PhotoImage(file="./images/card_front.png")
card_front = tkinter.Canvas(root, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front.create_image(400, 263, image=card_front_img)

# DEFAULT TITLE AND WORD
title = "French"
word = "English"
card_front.create_text(400, 150, text=f"{title}", font=FONT, tags="title")
card_front.create_text(400, 263, text=f"{word}", font=FONT, tags="word")
card_front.grid(row=0, column=0, columnspan=2)

# BUTTONS
incorrect_btn_img = PhotoImage(file="./images/wrong.png")
incorrect_btn = tkinter.Button(root, borderwidth=0, highlightthickness=0, image=incorrect_btn_img, command=incorrect)
incorrect_btn.grid(row=1, column=0)

correct_btn_img = PhotoImage(file="./images/right.png")
correct_btn = tkinter.Button(root, borderwidth=0, highlightthickness=0, image=correct_btn_img, command=correct)
correct_btn.grid(row=1, column=1)

root.mainloop()
