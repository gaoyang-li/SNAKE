from tkinter import *
import random
import ctypes
import pickle
Width = 1400
Height = 650
Colours = ["red", "orange", "yellow", "green", "indigo", "violet"]
MyFile = open("Scores.txt", "a")


def GetExit():
    DestroyMenu()


def DestroyMenu():
    windowMenu.destroy()


def GetHelp():
    windowStart = Tk()
    windowStart.title("HELP")
    windowStart.geometry("1100x550")
    windowStart.minsize(width=400, height=400)
    windowStart.maxsize(width=1500, height=700)
    windowStart.config(background="black")
    windowStart.attributes("-alpha", 1)
    windowStart.attributes("-topmost", 1)
    StartLabe2 = Label(windowStart, bg="black", fg="white",
                       text="Press 'W' 'A' 'S' 'D' to change the direction and move at a normal speeed ", font="Arial,400")
    StartLabe3 = Label(windowStart, bg="black", fg="white",
                       text="Press 'Up' 'Down' 'Left' 'Right' to change the direction and move at a faster speeed ", font="Arial,400")
    StartLabe4 = Label(windowStart, bg="black", fg="white",
                       text="Press 'P' To Pause", font="Arial,400")
    StartLabe5 = Label(windowStart, bg="black", fg="white",
                       text="Press 'B' To Hide The Game. Please Open A Picture In Advance. A picture named 'BossPicture.png' is provided", font="Arial,400")
    StartLabe6 = Label(windowStart, bg="black", fg="white",
                       text="Press 'C' To Cheat. The Snake Will NOT Die if Head Touches Body\n\tYour Name, Score and Position Will Be Saved In 'Scores.txt'", font="Arial,400")
    StartLabe2.pack()
    StartLabe3.pack()
    StartLabe4.pack()
    StartLabe5.pack()
    StartLabe6.pack()
    windowStart.mainloop()


def GetStart():
    DestroyMenu()
    import Animation


def GetResume():
    DestroyMenu()
    import ResumeFile


def CreateButtons():
    global windowMenu
    windowMenu = Tk()
    windowMenu.title("MENU")
    windowMenu.geometry("2000x800")
    windowMenu.config(background="yellow")
    Starting = PhotoImage(file="Start.png")
    Resuming = PhotoImage(file="Resume.png")
    Exiting = PhotoImage(file="Exit.png")
    Helping = PhotoImage(file="Help.png")
    But1 = Button(windowMenu, image=Starting, width="500",
                  height="200", command=GetStart)
    But2 = Button(windowMenu, image=Resuming, width="500",
                  height="200", command=GetResume)
    But4 = Button(windowMenu, image=Helping, width="500",
                  height="200", command=GetHelp)
    But3 = Button(windowMenu, image=Exiting, width="500",
                  height="200", command=GetExit)
    But1.pack()
    But2.pack()
    But4.pack()
    But3.pack()
    windowMenu.mainloop()


CreateButtons()
