BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

choosen_word = {}
known_words = []



try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict("records")

print(len(to_learn))

def pick_card():
    global choosen_word, flip
    window.after_cancel(flip)
    choosen_word = random.choice(to_learn)
    word_fr = choosen_word["French"]
    card_canvas.itemconfig(upper_word, text="French")
    card_canvas.itemconfig(lower_word, text=word_fr)
    card_canvas.itemconfig(canvas_image, image=front_image)
    flip = window.after(3000, flip_card)

def flip_card():
    word_en = choosen_word["English"]
    card_canvas.itemconfig(upper_word, text="English")
    card_canvas.itemconfig(lower_word, text=word_en)
    card_canvas.itemconfig(canvas_image, image=back_image)

def remove_card():
    to_learn.remove(choosen_word)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    pick_card()
    




window = Tk()
window.title("FlashCards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip = window.after(3000, flip_card)

card_canvas = Canvas(bg=BACKGROUND_COLOR , height=600, width=800, highlightthickness=0, borderwidth=0)
card_canvas.grid(row=0, column=0, columnspan=2)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
canvas_image = card_canvas.create_image(400, 270, image=front_image)
upper_word = card_canvas.create_text(400, 150, text="", font=("Ariel", 25, "italic") )
lower_word = card_canvas.create_text(400, 279, text="", font=("Ariel", 30, "bold") )
#Button
rb_image = PhotoImage(file="images/right.png")
wb_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=rb_image, highlightthickness=0, borderwidth=0, command=remove_card)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wb_image, highlightthickness=0, borderwidth=0, command=pick_card )
wrong_button.grid(row=1, column=0)




pick_card()













window.mainloop()