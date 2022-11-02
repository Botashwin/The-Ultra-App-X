"""
Libraries To Import (Use In Terminal Or Command Prompt: -
python3.10 -m pip install tk
python3.10 -m pip install pygame
python3.10 -m pip install Pillow
"""
import tkinter as tk
import sys
from tkinter import *
from tkinter import messagebox
import maincalc,mainmusic,mainrps,mainwordle
from PIL import Image, ImageTk

print("\n---------------------------------------------------------------")
print("          ¯\_(ツ)_/¯  The Ultra App X  ¯\_(ツ)_/¯           ")
print("---------------------------------------------------------------")
print("Available Apps: -")
print("1) Calculator ++")
print("2) Music Player 10.0")
print("3) Rock Papers Scissors Game (RPS)")
print("4) Wordle")
def calc():
    #screen.iconify()
    maincalc.main()
    #screen.deiconify()
def music():
    mainmusic.main()
def rps1():
    mainrps.main()
def wordle1():
    mainwordle.main()
def exit1():
    if messagebox.askokcancel("Exit","Do You Want To Quit? 🥺 "):
        screen.destroy()
        print("\nThank You For Using The Ultra App X .... ¯\_(ツ)_/¯")
        sys.exit()

screen = tk.Tk()
screen.title('The Ultra App X')
screen.iconbitmap(r'xicon.ico')
screen.geometry("900x400")
screen.iconbitmap(r'xicon.ico')
screen.configure(bg="black")

frame = Frame(screen, width=140, height=140)
frame.pack()
frame.place(x=80,y=80)
img = ImageTk.PhotoImage(Image.open("Calc.jpeg"))
label1 = Label(frame, image = img)
label1.pack()

frame2 = Frame(screen, width=140, height=140)
frame2.pack()
frame2.place(x=288,y=80)
img2 = ImageTk.PhotoImage(Image.open("musicplay.png"))
label2 = Label(frame2, image = img2)
label2.pack()

frame3 = Frame(screen, width=140, height=140)
frame3.pack()
frame3.place(x=510,y=80)
img3 = ImageTk.PhotoImage(Image.open("rps.png"))
label3 = Label(frame3, image = img3)
label3.pack()

frame4 = Frame(screen, width=140, height=140)
frame4.pack()
frame4.place(x=710,y=80)
img4 = ImageTk.PhotoImage(Image.open("wordle.png"))
label4 = Label(frame4, image = img4)
label4.pack()

calculator = Button(screen, text="Calculator", command=calc)
calculator.config(font=('Trebuchet MS', 20), highlightbackground="#FE0221", bg="white", fg="black", padx=7, pady=7)
calculator.place(x=80, y=250)

musicplayer = Button(screen, text="Music Player", command=music)
musicplayer.config(font=('Trebuchet MS', 20), highlightbackground="#FAFE02", bg="white", fg="black", padx=7, pady=7)
musicplayer.place(x=280, y=250)

rps = Button(screen, text="RPS", command=rps1)
rps.config(font=('Trebuchet MS', 20), highlightbackground="#1DFE02", bg="white", fg="black", padx=7, pady=7)
rps.place(x=545, y=250)

wordle = Button(screen, text="Wordle", command=wordle1)
wordle.config(font=('Trebuchet MS', 20), highlightbackground="#DF02FE", bg="white", fg="black", padx=7, pady=7)
wordle.place(x=720, y=250)

Exitbtn = Button(screen, text="Exit", command=exit1)
Exitbtn.config(font=('Trebuchet MS', 20), highlightbackground="#02FEFA", bg="white", fg="black", padx=7, pady=7)
Exitbtn.place(x=410, y=336)

screen.mainloop()
