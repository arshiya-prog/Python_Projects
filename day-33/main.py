import tkinter as tk
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)
      
window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="#C95C5C")

canvas = tk.Canvas(width=300, height=414, bg="#C95C5C", highlightthickness=0)
background_img = tk.PhotoImage(file="/Users/arshiya/Desktop/Coding/Python/Python_Projects/day-33/background.png")
canvas.create_image(150, 207, image=background_img)
response = requests.get(url="https://api.kanye.rest")
quote = response.json()["quote"]
quote_text = canvas.create_text(150, 207, text=f"{quote}", width=250, font=("Arial", 20, "bold"), fill="white")

canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="/Users/arshiya/Desktop/Coding/Python/Python_Projects/day-33/kanye.png")
small_kanye_img = tk.PhotoImage(file="/Users/arshiya/Desktop/Coding/Python/Python_Projects/day-33/dark_kanye.png")

label = tk.Label(window, image=kanye_img, bg="#C95C5C", cursor="hand2")
label.grid(row=1, column=0)

def on_press(event):
    label.config(image=small_kanye_img)

def on_release(event):
    label.config(image=kanye_img)
    get_quote()

label.bind("<ButtonPress-1>", on_press)
label.bind("<ButtonRelease-1>", on_release)

# kanye_button = tk.Button(
#     image=kanye_img,
#     command=get_quote,
#     bd=0,
#     borderwidth=0,
#     highlightthickness=0,
#     relief="flat",
#     takefocus=0,
# )
# kanye_button.grid(row=1, column=0)

window.mainloop()