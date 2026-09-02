import pandas as pd
import tkinter as tk
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
list_of_dicts = []

try:
    data = pd.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    og_data = pd.read_csv("data/french_words.csv")
    list_of_dicts = og_data.to_dict(orient="records")
else:
    list_of_dicts = data.to_dict(orient="records")


# ---------------------------- GENERATE NEW FLASHCARD AFTER CROSS ------------------------------- # 
def generate_flashcard():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=front_card_path)
    try:
        current_card = random.choice(list_of_dicts)
    except IndexError:
        canvas.itemconfig(word_label, text="No words left in the file.", font=("Ariel", 40, "bold"), fill="black")
    else:
        canvas.itemconfig(lang_label, text="French", fill="black")
        canvas.itemconfig(word_label, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP THE FLASHCARD ------------------------------- # 
def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_path)
    canvas.itemconfig(lang_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")


# ---------------------------- GENERATE NEW FLASHCARD AFTER TICK ------------------------------- # 
def is_known():
    try:
        list_of_dicts.remove(current_card)
    except ValueError:
        canvas.itemconfig(word_label, text="No words left in the file.", font=("Ariel", 40, "bold"), fill="black")
    
    df = pd.DataFrame(list_of_dicts)
    df.to_csv("data/words_to_learn.csv", index=False)

    generate_flashcard()


# ---------------------------- UI SETUP ------------------------------- # 
window = tk.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_path = tk.PhotoImage(file="images/card_front.png")
back_card_path = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_path)

lang_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

tick = tk.PhotoImage(file="images/right.png")
tick_button = tk.Button(image=tick, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
tick_button.grid(row=1, column=0)

cross = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=generate_flashcard)
cross_button.grid(row=1, column=1)

generate_flashcard()

window.mainloop()