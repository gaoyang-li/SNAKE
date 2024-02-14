from tkinter import *
import random
import ctypes
import pickle
IsResume = False


ResumeWindow = Tk()
ResumeWindow.title("RESUME")
ResumeWindow.geometry("500x500")
ResumeLabel = Label(
    ResumeWindow, text="Enter The File Name:(suffix not needed)", fg="purple")
ResumeLabel.pack()
Resumeentry = Entry(ResumeWindow, bd=4, fg="dark blue", cursor="cross")
Resumeentry.pack()


def GetFileName():
    global ResumeFileName
    global Resumelist_file
    global Score
    global UserName
    ResumeFileName = Resumeentry.get() + ".pkl"
    Resumelist_file = open(ResumeFileName, 'rb')
    ResumeWindow.destroy()


ResumeButtom1 = Button(ResumeWindow, text="CONFIRM", width=15,
                       height=2, command=GetFileName, bg="yellow", fg="red")
ResumeButtom1.pack()
ResumeWindow.mainloop()
Score = pickle.load(Resumelist_file)
UserName = pickle.load(Resumelist_file)
Score = int(Score)
UserName = str(UserName)

Width = 1400
Height = 650
Colours = ["red", "orange", "yellow", "green", "indigo", "violet"]
MyFile = open("Scores.txt", "a")
IsCheat = False


def HideGame():
    window.attributes("-alpha", 0)


def DisplayGame():
    window.attributes("-alpha", 1)


def CheatKey(event):
    global IsCheat
    IsCheat = True


def BossKey(event):
    global direction
    direction = "Boss"


def PauseKey(event):
    global direction
    direction = "Pause"


def MoreLeftKey(event):
    global direction
    direction = "moreleft"


def MoreRightKey(event):
    global direction
    direction = "moreright"


def MoreUpKey(event):
    global direction
    direction = "moreup"


def MoreDownKey(event):
    global direction
    direction = "moredown"


def LeftKey(event):
    global direction
    direction = "left"


def RightKey(event):
    global direction
    direction = "right"


def UpKey(event):
    global direction
    direction = "up"


def DownKey(event):
    global direction
    direction = "down"


def SetWindowDimension(w, h):
    global window
    window = Tk()
    window.title("SnakeGame")
    window.config(background="black")
    window.attributes("-alpha", 1)
    window.attributes("-topmost", 1)
    ScreenWidth = window.winfo_screenwidth()
    ScreenHeight = window.winfo_screenheight()
    x = (ScreenWidth/2)-(w/2)
    y = (ScreenHeight/2)-(h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window


def PlaceFood():
    global Food0
    global Food1
    global Food2
    global Colour
    global Number
    Colour = Colours[random.randint(0, 5)]
    Food0 = canvas.create_rectangle(0, 0, SnakeSize, SnakeSize, fill=Colour)
    Food1 = random.randint(0, Width-SnakeSize)
    Food2 = random.randint(0, Height-SnakeSize)
    canvas.move(Food0, Food1, Food2)


def MoveSnake():
    global IsPause
    global IsBoss
    global GameOver
    global SnakeHeadPosition
    global Positions
    global FoodPosition
    IsBoss = False
    IsPause = False
    GameOver = False
    canvas.pack()
    Positions = []
    Positions.append(canvas.coords(Snake[0]))

    if Positions[0][0] < 0 or Positions[0][2] > Width or Positions[0][3] > Height or Positions[0][1] < 0:
        GameOver = True
        canvas.create_text(Width/2, Height/2, fill="red",
                           font="Arial", text="GAME OVER\nScore:" + str(Score))
        MyFile.write(UserName + ": " + str(Score) + "\n")
        MyFile.close()
        Positions.clear()
        Positions.append(canvas.coords(Snake[0]))
    if direction == "left":
        canvas.move(Snake[0], -SnakeSize, 0)
        IsPause = False
        DisplayGame()
    elif direction == "right":
        canvas.move(Snake[0], SnakeSize, 0)
        IsPause = False
        DisplayGame()
    elif direction == "up":
        canvas.move(Snake[0], 0, -SnakeSize)
        IsPause = False
        DisplayGame()
    elif direction == "down":
        canvas.move(Snake[0], 0, SnakeSize)
        IsPause = False
        DisplayGame()
    elif direction == "moreleft":
        canvas.move(Snake[0], -SnakeSize-SnakeSize, 0)
        IsPause = False
        DisplayGame()
    elif direction == "moreright":
        canvas.move(Snake[0], SnakeSize+SnakeSize, 0)
        IsPause = False
        DisplayGame()
    elif direction == "moreup":
        canvas.move(Snake[0], 0, -SnakeSize-SnakeSize)
        IsPause = False
        DisplayGame()
    elif direction == "moredown":
        canvas.move(Snake[0], 0, SnakeSize+SnakeSize)
        IsPause = False
        DisplayGame()
    elif direction == "Pause":
        canvas.move(Snake[0], 0, 0)
        IsPause = True
        DisplayGame()
    elif direction == "Boss":
        canvas.move(Snake[0], 0, 0)
        IsPause = True
        IsBoss = True
        HideGame()

    SnakeHeadPosition = canvas.coords(Snake[0])
    FoodPosition = canvas.coords(Food0)
    if OverLapping(SnakeHeadPosition, FoodPosition):
        GrowSnake()
        MoveFood()
    for i in range(1, len(Snake)):
        if OverLapping(SnakeHeadPosition, canvas.coords(Snake[i])) and IsPause == False and IsBoss == False and IsCheat == False:
            GameOver = True
            canvas.create_text(Width/2, Height/2, fill="blue",
                               font="Arial", text="GAME OVER")
            MyFile.write(UserName + ": " + str(Score) + "\n")
            MyFile.close()
    if GameOver == False:
        window.after(90, MoveSnake)
    for i in range(1, len(Snake)):
        if IsPause == False and IsBoss == False:
            Positions.append(canvas.coords(Snake[i]))

    for i in range(len(Snake)-1):
        if IsPause == False and IsBoss == False:
            canvas.coords(Snake[i+1], Positions[i][0],
                          Positions[i][1], Positions[i][2], Positions[i][3])


def GrowSnake():
    global Score
    LastElement = len(Snake) - 1
    LastElementPosition = canvas.coords(Snake[LastElement])
    Snake.append(canvas.create_oval(0, 0, SnakeSize, SnakeSize, fill=Colour))
    if direction == "left" or direction == "moreleft":
        canvas.coords(Snake[LastElement+1], LastElementPosition[0] + SnakeSize,
                      LastElementPosition[1], LastElementPosition[2] + SnakeSize, LastElementPosition[3])
    elif direction == "right" or direction == "moreright":
        canvas.coords(Snake[LastElement+1], LastElementPosition[0] - SnakeSize,
                      LastElementPosition[1], LastElementPosition[2] - SnakeSize, LastElementPosition[3])
    elif direction == "up" or direction == "moreup":
        canvas.coords(Snake[LastElement+1], LastElementPosition[0], LastElementPosition[1] +
                      SnakeSize, LastElementPosition[2], LastElementPosition[3] + SnakeSize)
    elif direction == "down" or direction == "moredown":
        canvas.coords(Snake[LastElement+1], LastElementPosition[0], LastElementPosition[1] -
                      SnakeSize, LastElementPosition[2], LastElementPosition[3]-SnakeSize)
    Score = Score + 1
    txt = "score:" + str(Score)
    canvas.itemconfigure(ScoreText, text=txt)


def MoveFood():
    global Food0
    global Food1
    global Food2
    global Colour
    canvas.move(Food0, (Food1*(-2)), (Food2*(-2)))
    Colour = Colours[random.randint(0, 5)]
    Food0 = canvas.create_rectangle(0, 0, SnakeSize, SnakeSize, fill=Colour)
    Food1 = random.randint(0, Width-SnakeSize)
    Food2 = random.randint(0, Height-SnakeSize)
    canvas.move(Food0, Food1, Food2)


def OverLapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


window = SetWindowDimension(Width, Height)
canvas = Canvas(window, bg="black", width=Width, height=Height)
Snake = []
SnakeSize = 15

Snake.append(canvas.create_oval(SnakeSize, SnakeSize,
             SnakeSize*2, SnakeSize*2, fill="white"))

Text = "Score: " + str(Score)
ScoreText = canvas.create_text(
    Width/2, 10, fill="brown", font="Arial", text=Text)


canvas.bind("<A>", LeftKey)
canvas.bind("<D>", RightKey)
canvas.bind("<W>", UpKey)
canvas.bind("<S>", DownKey)
canvas.bind("<a>", LeftKey)
canvas.bind("<d>", RightKey)
canvas.bind("<w>", UpKey)
canvas.bind("<s>", DownKey)
canvas.bind("<Left>", MoreLeftKey)
canvas.bind("<Right>", MoreRightKey)
canvas.bind("<Up>", MoreUpKey)
canvas.bind("<Down>", MoreDownKey)
canvas.bind("<P>", PauseKey)
canvas.bind("<p>", PauseKey)
canvas.bind("<B>", BossKey)
canvas.bind("<b>", BossKey)
canvas.bind("<C>", CheatKey)
canvas.bind("<c>", CheatKey)
canvas.focus_set()
direction = "right"

PlaceFood()
MoveSnake()
window.mainloop()


SaveWindow = Tk()
SaveWindow.title("SAVE")
SaveWindow.geometry("600x200")
SaveLabel = Label(
    SaveWindow, text="Save Your Name&Score In A File? If Not, just close the page", fg="purple")
SaveLabel.pack()
Saveentry = Entry(SaveWindow, bd=4, fg="dark blue", cursor="cross")
Saveentry.pack()


def GetFile():
    global FileName
    FileName = Saveentry.get() + ".pkl"
    list_file = open(FileName, 'wb')
    pickle.dump(Score, list_file)
    list_file.close()
    SaveWindow.destroy()


SaveButtom1 = Button(SaveWindow, text="CONFIRM", width=15,
                     height=2, command=GetFile, bg="yellow", fg="red")
SaveButtom1.pack()
SaveWindow.mainloop()


FileList = []
NextFileList = []
Dic = {}
ScoreList = []

ThisFile = open("Scores.txt", "r")
FileContent = ThisFile.readline().strip()
FileList.append(FileContent)

while len(FileContent) > 0:
    FileContent = ThisFile.readline().strip()
    FileList.append(FileContent)
FileList.pop()
ThisFile.close()


for i in range(0, len(FileList)):
    FileGet = FileList[i]
    ColonIndex = int(FileGet.index(":"))
    BeginIndex = ColonIndex + 1
    TheName = str(FileGet[0:ColonIndex+1])
    TheScore = str(FileGet[BeginIndex+1:])
    NewDic = {TheScore: TheName}
    Dic.update(NewDic)
    NextFileList.append(FileGet[BeginIndex:])
    NextFileList.sort()

for Item in Dic.items():
    ScoreList.append(Item)
ScoreList.sort()

TempFile = open("Scores.txt", "w")
TempFile.write("")
TempFile.close

ThatFile = open("Scores.txt", "a")
for j in range(0, len(ScoreList)):
    Scorelist = (ScoreList[j])
    Message = Scorelist[1] + " " + Scorelist[0] + "\n"
    ThatFile.write(Message)
ThatFile.close()
