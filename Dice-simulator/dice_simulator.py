import tkinter as tk
from PIL import Image,ImageTk
import random

dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]

root = tk.Tk()
root.title("Dice Simulator")
root.geometry("450x250")

m1 = tk.Label(root,text='Hello, from Raj.!',fg="red",bg="black",font="Helvetica 16 bold")
m1.pack()
img=ImageTk.PhotoImage(Image.open(random.choice(dice)))

m2 = tk.Label(root,image=img)
m2.image=img
m2.pack()

def roll():
    img=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    m2.configure(image=img)
    m2.image=img

button = tk.Button(root,text='Roll the Dice',fg='red',command=roll)
button.pack()

root.mainloop()
