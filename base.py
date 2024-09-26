import os
import sys
import tkinter as tk
from tkinter import *
import pygame

pygame.init()
win = tk.Tk()

win.geometry("800x600")
win.configure(bg="#0E1C27")


def click1():
    os.chdir("C:/Users/samso/OneDrive/Documents/tkinter/TIC TAC")
    os.system("python3 tictac.py")


def click2():
    os.chdir("C:/Users/samso/OneDrive/Documents/tkinter/Space War")
    os.system("python3 main.py")


def click3():
    os.chdir("C:/Users/samso/OneDrive/Documents/tkinter/Flappybird")
    os.system("python3 main.py")


def click4():
    os.chdir("C:/Users/samso/OneDrive/Documents/tkinter/Connect4U")
    os.system("python3 connect4u.py")


btn1 = tk.Button(
    win, text="TIC TAC TOE", command=click1, bg="#1167B1", height=4, width=30
)
btn1.place(relx=0.5, rely=0.38, anchor="center")
btn2 = tk.Button(
    win, text="Space Wars", command=click2, bg="#1167B1", height=4, width=30
)
btn2.place(relx=0.5, rely=0.5, anchor="center")
btn3 = tk.Button(
    win, text="Flappy Bird", command=click3, bg="#1167B1", height=4, width=30
)
btn3.place(relx=0.5, rely=0.62, anchor="center")
btn4 = tk.Button(
    win, text="Connect4U", command=click4, bg="#1167B1", height=4, width=30
)
btn4.place(relx=0.5, rely=0.74, anchor="center")
win.mainloop()
