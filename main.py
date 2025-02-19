import tkinter
from lib2to3.pgen2.pgen import PgenGrammar
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

# MAIN WINDOW
root = tkinter.Tk()
root.title("Flash Card App")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# WIDGETS INSIDE CANVAS
card_front_img = PhotoImage(file="./images/card_front.png")
card_front = tkinter.Canvas(root, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front.create_image(400, 263, image=card_front_img)
card_front.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_front.create_text(400, 263, text="Word", font=("Arial", 40, "bold"))
card_front.grid(row=0, column=0, columnspan=2)

# BUTTONS
incorrect_btn_img = PhotoImage(file="./images/wrong.png")
correct_btn_img = PhotoImage(file="./images/right.png")
incorrect_btn = tkinter.Button(root, borderwidth=0, highlightthickness=0, image=incorrect_btn_img)
incorrect_btn.grid(row=1, column=0)

correct_btn = tkinter.Button(root, borderwidth=0, highlightthickness=0, image=correct_btn_img)
correct_btn.grid(row=1, column=1)

root.mainloop()
