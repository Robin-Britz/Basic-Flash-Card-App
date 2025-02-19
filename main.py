import tkinter
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

# MAIN WINDOW
root = tkinter.Tk()
root.title("Flash Card App")
root.config(bg=BACKGROUND_COLOR)

# FRAME INSIDE WINDOW
frame = tkinter.Frame(root, padx=50, pady=50)
frame.grid()

# WIDGETS IN FRAME
title_label = tkinter.Label(frame)
title_label.config(text="title")
title_label.grid(row=0, column=1)

answer_label = tkinter.Label(frame)
answer_label.config(text="WORD")
answer_label.grid(row=1, column=1)

# BUTTON IMAGES
incorrect_btn_image = PhotoImage(file="./images/wrong.png")
correct_btn_image = PhotoImage(file="./images/right.png")

# BUTTONS
incorrect_btn = tkinter.Button(root, borderwidth=0, highlightthickness=0, image=incorrect_btn_image, bg="#000000")
incorrect_btn.grid(row=2, column=0)

correct_btn = tkinter.Button(root, borderwidth=0, highlightthickness=0, image=correct_btn_image, bg="#000000")
correct_btn.grid(row=2, column=1)

root.mainloop()
