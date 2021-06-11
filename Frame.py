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

    def start_playing(self):
        self.start.destroy()
        if self.computer_side == "player1":
            self.current_player = "player2"
            self.ai_play["state"] = "normal"
        else:
            self.ai_play["state"] = "disabled"
        self.update_labels()


    def update_labels(self):


        if self.current_player=="player1":

            self.b0["state"] = "normal"
            self.b1["state"] = "normal"
            self.b2["state"] = "normal"
            self.b3["state"] = "normal"
            self.b4["state"] = "normal"
            self.b5["state"] = "normal"
            for i in range(6):
                if self.player[i] == 0:
                    if i == 0:
                        self.b0["state"] = "disabled"
                    if i == 1:
                        self.b1["state"] = "disabled"
                    if i == 2:
                        self.b2["state"] = "disabled"
                    if i == 3:
                        self.b3["state"] = "disabled"
                    if i == 4:
                        self.b4["state"] = "disabled"
                    if i == 5:
                        self.b5["state"] = "disabled"

            if not self.computer:
                self.b7["state"] = "disabled"
                self.b8["state"] = "disabled"
                self.b9["state"] = "disabled"
                self.b10["state"] = "disabled"
                self.b11["state"] = "disabled"
                self.b12["state"] = "disabled"
        if self.current_player=="player2":
            if not self.computer:
                self.b7["state"] = "normal"
                self.b8["state"] = "normal"
                self.b9["state"] = "normal"
                self.b10["state"] = "normal"
                self.b11["state"] = "normal"
                self.b12["state"] = "normal"
                for i in range(13)[7:]:
                    if self.player[i] == 0:
                        if i == 7:
                            self.b7["state"] = "disabled"
                        if i == 8:
                            self.b8["state"] = "disabled"
                        if i == 9:
                            self.b9["state"] = "disabled"
                        if i == 10:
                            self.b10["state"] = "disabled"
                        if i == 11:
                            self.b11["state"] = "disabled"
                        if i == 12:
                            self.b12["state"] = "disabled"

            self.b0["state"] = "disabled"
            self.b1["state"] = "disabled"
            self.b2["state"] = "disabled"
            self.b3["state"] = "disabled"
            self.b4["state"] = "disabled"
            self.b5["state"] = "disabled"




        self.l0 = Label(self.master, text=self.player[0], width=2, height=1, font="Helvetica 14 ",
                        bg="orange", fg="black")
        self.l0.place(x=190, y=530)
        self.l1 = Label(self.master, text=self.player[1], width=2, height=1, font="Helvetica 14 ",
                        bg="orange", fg="black")
        self.l1.place(x=310, y=530)
        self.l2 = Label(self.master, text=self.player[2], width=2, height=1, font="Helvetica 14 ",
                        bg="orange", fg="black")
        self.l2.place(x=430, y=530)
        self.l3 = Label(self.master, text=self.player[3], width=2, height=1, font="Helvetica 14 ",
                        bg="orange", fg="black")
        self.l3.place(x=550, y=530)
        self.l4 = Label(self.master, text=self.player[4], width=2, height=1, font="Helvetica 14 ",
                        bg="orange", fg="black")
        self.l4.place(x=670, y=530)
        self.l5 = Label(self.master, text=self.player[5], width=2, height=1, font="Helvetica 14 ",
                        bg="orange", fg="black")
        self.l5.place(x=790, y=530)

        self.l7 = Label(self.master, text=self.player[12], width=2, height=1, font="Helvetica 14 ",
                        bg="cyan", fg="green")
        self.l7.place(x=190, y=150)
        self.l8 = Label(self.master, text=self.player[11], width=2, height=1, font="Helvetica 14 ",
                        bg="cyan", fg="green")
        self.l8.place(x=310, y=150)
        self.l9 = Label(self.master, text=self.player[10], width=2, height=1, font="Helvetica 14 ",
                        bg="cyan", fg="green")
        self.l9.place(x=430, y=150)
        self.l10 = Label(self.master, text=self.player[9], width=2, height=1, font="Helvetica 14 ",
                         bg="cyan", fg="green")
        self.l10.place(x=550, y=150)
        self.l11 = Label(self.master, text=self.player[8], width=2, height=1, font="Helvetica 14 ",
                         bg="cyan", fg="green")
        self.l11.place(x=670, y=150)
        self.l12 = Label(self.master, text=self.player[7], width=2, height=1, font="Helvetica 14 ",
                         bg="cyan", fg="green")
        self.l12.place(x=790, y=150)

        self.l6 = Label(self.master, text=self.player[6], width=3, height=1, font="Helvetica 20 ",
                        bg="orange", fg="black")
        self.l6.place(x=900, y=330)
        self.l13 = Label(self.master, text=self.player[13], width=2, height=1, font="Helvetica 20 ",
                         bg="cyan", fg="green")
        self.l13.place(x=80, y=330)
        state1=state(self.player,0,"player1","With Stealing")
        if state1.newTurn() =="finish":
            self.b0["state"] = "disabled"
            self.b1["state"] = "disabled"
            self.b2["state"] = "disabled"
            self.b3["state"] = "disabled"
            self.b4["state"] = "disabled"
            self.b5["state"] = "disabled"

    def compuer_play(self):


        diff=self.clicked1.get()



        computer = node(self.player, "player2", self.mode)
        if diff=="Easy":
            computer.set_depth(3)
        if diff=="Medium":
            computer.set_depth(6)
        if diff=="Hard":
            computer.set_depth(9)


        move = GET_AI_MOVE(computer, 1, True, -5000000, 5000000)
        A = state(self.player, move, "player2", self.mode)
        self.player = A.nextState()
        self.ai_play["state"] = "disabled"

        self.current_player = "player1"
        if A.nextTurn=="player2":
            self.current_player = "player2"
            self.ai_play["state"] = "normal"


        self.update_labels()