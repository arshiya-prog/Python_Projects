THEME_COLOR = "#375362"
import tkinter as tk

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = tk.Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.correct = tk.PhotoImage(file="day-34/images/true.png")
        self.correct_button = tk.Button(image=self.correct, padx=20, pady=20, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.correct_button.grid(row=2, column=0)

        self.wrong = tk.PhotoImage(file="day-34/images/false.png")
        self.wrong_button = tk.Button(image=self.wrong, padx=20, pady=20, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()