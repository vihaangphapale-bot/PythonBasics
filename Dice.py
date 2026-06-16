import tkinter as tk
import random
def roll():
    num = str(random.randint(1, 6))
    word.config(text=num)

root = tk.Tk()
button = tk.Button(root, text="Random", width=25, command=roll)
button.pack()
button2 = tk.Button(root, text="Stop", width=25, command=root.destroy)
button2.pack()
word = tk.Label(root, text="1", font=("Arial", 100))
word.pack(pady=20)
root.title("Dice Rolling")
root.mainloop()