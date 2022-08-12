import tkinter as tk
from tkinter import Label, ttk
import random
import sys

class window(tk.Tk):
    def __init__(self, *,
    main = False,
    num = 0,
    path = "",
    fontsize = 0,
    pack_ = True
    ):
        super().__init__()
        self.num = num
        self.resizable(0, 0)
        self.state('zoomed')
        self.configure(bg = "#B0E0E6")
        self.title("Trollgame")
        self.iconbitmap("./assets/icon.ico")
        self.attributes("-topmost", 1)
        self.photo = tk.PhotoImage(file = path)
        self.pack_ = pack_
        self.protocol("WM_DELETE_WINDOW", sys.exit)
       
        if not main:
            self.nextButton = ttk.Button(self,
            text = "Next level >>",
            command = self.destroy
            )
            self.nextButton.state(["disabled"])
            self.nextButton.pack(side = "right", fill = "both")

            ttk.Label(self, background = "#B0E0E6").pack(ipady = 50)
            self.mission = ttk.Label(self,
            text = f"Click the button {num} times",
            background = "#B0E0E6",
            font = ("Times New Roman", fontsize)
            )
            self.button = ttk.Button(self, text = "Click me!", command = self.click)
            self.button.pack(pady = 10, ipadx = 10, ipady = 10)
            self.mission.pack()

    def click(self):
        if self.num !=0:
            self.num -=1
            self.mission.config(text = f"Click the button {self.num} times")
        if self.num <= 0:
            self.button.state(["disabled"])
            self.nextButton.state(["!disabled"])
            if not self.pack_:
                ttk.Label(self, image = self.photo).place(x = self.winfo_screenwidth() // 2 ,
                y = self.winfo_screenheight() // 2,
                anchor = "center")
                ttk.Label(self,
                text = "Gameover!!",
                font = ("Times New Roman", 50),
                background = "#B0E0E6").place(x = 0, y = 0)
            else:
                ttk.Label(self, image = self.photo).pack()
                rantext = random.choice(["Quào!", "Amazing, good chóp!", "Giỏi quá!", "Vỗ tay!!!", "Amazing!", "Good job!", "Đúng là thằng em t!"]) 
                ttk.Label(self,
                text = rantext,
                font = ("Times New Roman", 20),
                background = "#B0E0E6"
                ).pack(ipady = 10)
    