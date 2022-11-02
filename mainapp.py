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
import maincalc,mainmusic,mainrps
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
def rps():
    mainrps.main()
def exit():
    if messagebox.askokcancel("Exit","Do You Want To Quit? 🥺 "):
        screen.destroy()
        print("\nThank You For Using The Ultra App X .... ¯\_(ツ)_/¯")
        sys.exit()

screen = tk.Tk()
screen.title('The Ultra App X')
'''screen.iconbitmap(r')'''
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


calculator = Button(screen, text="Calculator", command=calc)
calculator.config(font=('Trebuchet MS', 20), highlightbackground="#FE0221", bg="white", fg="black", padx=7, pady=7)
calculator.place(x=80, y=250)

musicplayer = Button(screen, text="Music Player", command=music)
musicplayer.config(font=('Trebuchet MS', 20), highlightbackground="#FAFE02", bg="white", fg="black", padx=7, pady=7)
musicplayer.place(x=280, y=250)

Exitbtn = Button(screen, text="Exit", command=exit)
Exitbtn.config(font=('Trebuchet MS', 20), highlightbackground="#02FEFA", bg="white", fg="black", padx=7, pady=7)
Exitbtn.place(x=410, y=336)

screen.mainloop()
