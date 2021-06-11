from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from State import state
from Node import  node
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

    def Play(self):

        if self.clicked2.get() == "Computer vs Player":

            self.computer = True
        else:
            self.computer = False

        if self.computer:
            self.player_side = self.clicked3.get()

            if self.player_side == "player1":
                self.computer_side = "player2"
            else:
                self.computer_side = "player1"
        else:
            self.computer_side = ""

        self.mode = self.clicked.get()

        self.player = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

        self.root.pack_forget()
        self.root.destroy()
        img = ImageTk.PhotoImage(Image.open("Mancala_Image.jpg"))
        my_label = Label(self.master, image=img)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ai_play = Button(self.master, text="AI Play", command=self.compuer_play, width=6, height=1,
                              font="Helvetica 20 ",
                              bg="white", fg="black")
        if self.computer:
            self.ai_play.place(x=40, y=50)
        self.start = Button(self.master, text="Start", command=self.start_playing, width=5, height=1,
                            font="Helvetica 25 ",
                            bg="white", fg="black")
        self.start.place(x=475, y=300)
        self.b0 = Button(self.master, text="Move", command=self.move0, width=4, height=1, font="Helvetica 14 ",
                         bg="orange", fg="black")
        self.b0.place(x=190, y=605)
        self.b1 = Button(self.master, text="Move", command=self.move1, width=4, height=1, font="Helvetica 14 ",
                         bg="orange", fg="black")
        self.b1.place(x=310, y=605)
        self.b2 = Button(self.master, text="Move", command=self.move2, width=4, height=1, font="Helvetica 14 ",
                         bg="orange", fg="black")
        self.b2.place(x=430, y=605)
        self.b3 = Button(self.master, text="Move", command=self.move3, width=4, height=1, font="Helvetica 14 ",
                         bg="orange", fg="black")
        self.b3.place(x=550, y=605)
        self.b4 = Button(self.master, text="Move", command=self.move4, width=4, height=1, font="Helvetica 14 ",
                         bg="orange", fg="black")
        self.b4.place(x=670, y=605)
        self.b5 = Button(self.master, text="Move", command=self.move5, width=4, height=1, font="Helvetica 14 ",
                         bg="orange", fg="black")
        self.b5.place(x=790, y=605)
        if not self.computer:
            self.b12 = Button(self.master, text="Move", command=self.move12, width=4, height=1, font="Helvetica 14 ",
                              bg="cyan", fg="green")
            self.b12.place(x=190, y=50)
            self.b11 = Button(self.master, text="Move", command=self.move11, width=4, height=1, font="Helvetica 14 ",
                              bg="cyan", fg="green")
            self.b11.place(x=310, y=50)
            self.b10 = Button(self.master, text="Move", command=self.move10, width=4, height=1, font="Helvetica 14 ",
                              bg="cyan", fg="green")
            self.b10.place(x=430, y=50)
            self.b9 = Button(self.master, text="Move", command=self.move9, width=4, height=1, font="Helvetica 14 ",
                             bg="cyan", fg="green")
            self.b9.place(x=550, y=50)
            self.b8 = Button(self.master, text="Move", command=self.move8, width=4, height=1, font="Helvetica 14 ",
                             bg="cyan", fg="green")
            self.b8.place(x=670, y=50)
            self.b7 = Button(self.master, text="Move", command=self.move7, width=4, height=1, font="Helvetica 14 ",
                             bg="cyan", fg="green")
            self.b7.place(x=790, y=50)
            self.b7["state"] = "disabled"
            self.b8["state"] = "disabled"
            self.b9["state"] = "disabled"
            self.b10["state"] = "disabled"
            self.b11["state"] = "disabled"
            self.b12["state"] = "disabled"

        self.b0["state"] = "disabled"
        self.b1["state"] = "disabled"
        self.b2["state"] = "disabled"
        self.b3["state"] = "disabled"
        self.b4["state"] = "disabled"
        self.b5["state"] = "disabled"
        self.ai_play["state"] = "disabled"

        reset_b = Button(self.master, text=" Reset ", command=self.reset, width=5, height=1, font="Helvetica 16 bold",
                         bg="grey")
        reset_b.pack(side=BOTTOM)

        self.master.mainloop()

    def save1(self):

        if (self.clicked2.get() == "Computer vs Player"):
            self.your_turn.pack()
            self.starting.pack(pady=5)

        self.Play_Button.pack(pady=10)
