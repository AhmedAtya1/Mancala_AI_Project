from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from State import state
from node import  node
from BestMove import  *
import time

class frame1:
    def __init__(self):
        self.master=Tk()
        self.master.title("Mancala Game")
        self.master.geometry("1024x700")
        self.root = Frame(self.master)
        self.root.pack()
        self.current_player="player1"
        self.Welcome = Label(self.root, text="Welcome To Mancala Game", font="Helvetica 50 italic")
        self.Welcome.pack(pady=30)
        self.clicked = StringVar()
        self.clicked.set("With Stealing")
        self.modee = Label(self.root, text="Please Select Game Settings ", font="Helvetica 25 italic")
        self.modee.pack()
        self.drop = OptionMenu(self.root, self.clicked, "With Stealing", "Without Stealing")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.drop.config(font=helv20)
        menu = self.root.nametowidget(self.drop.menuname)
        menu.config(font=helv20)  # Set the dropdown menu's font
        self.drop.pack(pady=10)

        self.clicked1 = StringVar()
        self.clicked1.set("Medium")

        self.Difficulty = OptionMenu(self.root, self.clicked1,"Easy" ,"Medium", "Hard")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.Difficulty.config(font=helv20)
        menu = self.root.nametowidget(self.Difficulty.menuname)
        menu.config(font=helv20)  # Set the dropdown menu's font
        self.Difficulty.pack(pady=10)

        self.clicked2 = StringVar()
        self.clicked2.set("Player vs Player")

        self.comp = OptionMenu(self.root, self.clicked2,  "Player vs Player", "Computer vs Player")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.comp .config(font=helv20)
        menu = self.root.nametowidget(self.comp .menuname)
        menu.config(font=helv20)  # Set the dropdown menu's font
        self.comp .pack(pady=10)

        self.clicked3 = StringVar()
        self.clicked3.set("player1")

        self.your_turn = Label(self.root, text="Please select side", font="Helvetica 25 italic")


        self.starting = OptionMenu(self.root, self.clicked3, "player1", "player2")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.starting.config(font=helv20)
        menu = self.root.nametowidget(self.starting.menuname)
        menu.config(font=helv20)
        self.save_settings=Button(self.root, text=" Save Settings ", command=self.save1, font="Helvetica 20 ", width=12)
        self.save_settings.pack(pady=20)



        self.Play_Button = Button(self.root, text=" Play ", command=self.Play, font="Helvetica 25 ", width=5)

        self.mode = ""
        self.master.mainloop()

    def reset(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Mancala Game")
        self.master.geometry("1024x700")
        self.root = Frame(self.master)
        self.root.pack()
        self.current_player = "player1"
        self.Welcome = Label(self.root, text="Welcome To Mancala Game", font="Helvetica 50 italic")
        self.Welcome.pack(pady=30)
        self.clicked = StringVar()
        self.clicked.set("With Stealing")
        self.modee = Label(self.root, text="Please Select Game Settings ", font="Helvetica 25 italic")
        self.modee.pack()
        self.drop = OptionMenu(self.root, self.clicked, "With Stealing", "Without Stealing")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.drop.config(font=helv20)
        menu = self.root.nametowidget(self.drop.menuname)
        menu.config(font=helv20)  # Set the dropdown menu's font
        self.drop.pack(pady=10)

        self.clicked1 = StringVar()
        self.clicked1.set("Medium")

        self.Difficulty = OptionMenu(self.root, self.clicked1, "Easy", "Medium", "Hard")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.Difficulty.config(font=helv20)
        menu = self.root.nametowidget(self.Difficulty.menuname)
        menu.config(font=helv20)  # Set the dropdown menu's font
        self.Difficulty.pack(pady=10)

        self.clicked2 = StringVar()
        self.clicked2.set("Player vs Player")

        self.comp = OptionMenu(self.root, self.clicked2, "Player vs Player", "Computer vs Player")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.comp.config(font=helv20)
        menu = self.root.nametowidget(self.comp.menuname)
        menu.config(font=helv20)  # Set the dropdown menu's font
        self.comp.pack(pady=10)

        self.clicked3 = StringVar()
        self.clicked3.set("player1")

        self.your_turn = Label(self.root, text="Please select side", font="Helvetica 20 italic")

        self.starting = OptionMenu(self.root, self.clicked3, "player1", "player2")
        helv20 = tkFont.Font(family='Helvetica', size=20)
        self.starting.config(font=helv20)
        menu = self.root.nametowidget(self.starting.menuname)
        menu.config(font=helv20)
        self.save_settings = Button(self.root, text=" Save Settings ", command=self.save1, font="Helvetica 20 ",
                                    width=12)
        self.save_settings.pack(pady=20)

        self.Play_Button = Button(self.root, text=" Play ", command=self.Play, font="Helvetica 25 ", width=5)

        self.mode = ""
        self.master.mainloop()
