from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
si_no = None





#-------------------------Functions---------------------------------------


def correct_button():
    global si_no
    df = pd.read_csv("data/french_words.csv")
    si_no = random.randint(0, len(df)-1)
    print(si_no)
    french = df.loc[si_no, "French"]
    canvas.itemconfig(text_item, text=french)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(canvas_image, image=card_font)
    window.after(3000, english_button)


def english_button():
    df = pd.read_csv("data/french_words.csv")
    global si_no
    english = df.loc[si_no, "English"]
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(text_item, text=english)
    canvas.itemconfig(title, text="English")

def remove():
    global si_no
    df = pd.read_csv("data/french_words.csv")
    si_no = int(si_no)
    data = df.loc[si_no, "French"]
    print(data)
    df.drop(si_no, inplace=True)
    df.to_csv(path_or_buf="data/french_words.csv", index=False)
    correct_button()


#-------------------------------UI----------------------------------------
window = Tk()
window.title("Flashyy")
window.config(padx=50, pady=40,background=BACKGROUND_COLOR)

canvas = Canvas(window,height=526, width=800, background=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)

card_font = PhotoImage(file="images/card_front.png")


canvas_image = canvas.create_image(410,270, image=card_font)
title = canvas.create_text(400, 150, fill="black", font="Ariel 40 italic", text="French")
text_item = canvas.create_text(400, 263, fill="black", font="Ariel 60 bold", text="French")
canvas.grid(row=0, column=0, columnspan=2, pady=20)

dum = correct_button()
canvas.itemconfig(text_item,text=dum)

right_img = PhotoImage(file="images/right.png")
right_button = Button(text="click me", image=right_img,command=remove)
right_button.grid(row=1, column=0)
card_back = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=correct_button)
wrong_button.grid(row=1, column=1)
window.after(3000, func=english_button)

window.mainloop()
