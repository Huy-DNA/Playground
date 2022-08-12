import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
import random
from info import * 
from color_funcs import *

class Screen():
    def __init__(self):
        self.stop = False
        self.root = tk.Tk()
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        posx = (screenWidth - winWidth) // 2
        posy = (screenHeight - winHeight) // 2
        self.root.geometry(f"{winWidth}x{winHeight}+{posx}+{posy}")
        self.root.title("Color Guessing Game")
        self.root.resizable(0, 0)
        self.root.iconbitmap("icon.ico")
        self.gameTitle = tk.Label(self.root, text = "Colour Guessing Game",
                                font = (fontuse, bigfont), fg = "white")
        self.gameTitle.pack(ipady = 120)
        self.startButton = tk.Button(self.root, text = "Start",
                                    width = 20, height = 5, command = self.startGame)
        self.startButton.pack()
        self.changebkg()
        self.level = 0
        
    def changebkg(self):
        if not self.stop:
            bkgcolor = color_to_hex(random.choice((allcolor)))
            self.root.configure(bg = bkgcolor)
            self.gameTitle.config(bg = bkgcolor)
            self.root.after(400, self.changebkg)

    def startGame(self):
        self.startButton.destroy()
        self.gameTitle.destroy()
        self.root.configure(bg = "white")
        self.stop = True
        self.level += 1
        if self.level <= 3:
            difficulty = "easy"
        elif self.level <= 6:
            difficulty = "intermediate"
        elif self.level <= 9:
            difficulty = "hard"
        else:
            difficulty = random.choice(["intermediate", "hard", "easy"])
        self.startLevel(self.level, difficulty)

    class createFrameUtility():
        def __init__(self, outer, level, difficulty):
            self.outer = outer
            self.difficulty = difficulty
            self.frameUtility = ttk.Frame(self.outer.root)
            tk.Label(self.frameUtility).pack(pady = 20) #initial spacing
            
            self.timerLabel = tk.Label(self.frameUtility, text = "Timer",
                                            font = (fontuse, medfont))
            self.timerLabel.pack(ipady = 10)
            self.timevar = tk.IntVar()
            self.timevar.set(6)
            self.time = tk.Label(self.frameUtility, textvariable = self.timevar,
                                    font = (fontuse, medfont))
            self.time.pack()
            self.decTime()
            
            self.level = tk.Label(self.frameUtility, text = f"Level {level}",
                                        font = (fontuse, smallfont))
            self.level.pack(ipady = 30)

            self.accuracyLabel = tk.Label(self.frameUtility, text = "Accuracy: ",
                                                font = (fontuse, smallfont))
            self.accuracyLabel.pack(ipady = 10)
            self.outer.accuracy = random.choice(accuracydict[difficulty])
            self.accuracyDisplay = tk.Label(self.frameUtility,
                                    text = str(self.outer.accuracy) + "%")
            self.accuracyDisplay.pack()
        def __call__(self):
            return self.frameUtility
        def decTime(self):
            time = self.timevar.get()
            if time > 1:
                self.timevar.set(time - 1)
                self.outer.root.after(1000, self.decTime)
            else:
                self.timevar.set(time - 1)
                self.outer.canvasShowColor.config(bg = "white")
                self.outer.yourrgb = tuple([int(i) for i in askcolor()[0]])
                self.outer.yourAccuracy = colorCompare(self.outer.myrgb, self.outer.yourrgb)
                self.outer.showResult(self.outer.myrgb, self.outer.yourrgb,
                                    self.outer.accuracy, self.outer.yourAccuracy)

    def showColor(self):
        bkgcolor = random.choice(allcolor)
        return bkgcolor

    def startLevel(self, level, difficulty):
        self.wholeframeUtility = self.createFrameUtility(self, level, difficulty)
        self.frameUtility = self.wholeframeUtility()
        self.frameUtility.pack(side = "right", fill = "both", ipadx = 50)
        self.myrgb = self.showColor()
        self.canvasShowColor = tk.Canvas(self.root,
        height = winHeight, bg = color_to_hex(self.myrgb))
        self.canvasShowColor.pack(fill = "both")
    
    def showResult(self, myrgb, yourrgb, accuracy, yourAccuracy):
        myrgb = color_to_hex(myrgb)
        yourrgb = color_to_hex(yourrgb)
        self.canvasShowColor.create_rectangle(0, 0, 600, winHeight // 2,
                                            fill = myrgb)
        self.canvasShowColor.create_text(200, winHeight // 4,
                                        text = "My Colour", font = (fontuse, medfont))
        self.canvasShowColor.create_text(200, winHeight // 4 + 30,
                        text = f"Required Accuracy: {accuracy}%", font = (fontuse, medfont))

        self.canvasShowColor.create_rectangle(0, winHeight // 2, 600, winHeight,
                                            fill = yourrgb)
        self.canvasShowColor.create_text(200, 3 * winHeight // 4,
                                        text = "Your Color", font = (fontuse, medfont))
        self.canvasShowColor.create_text(200, 3 * winHeight // 4 + 30,
            text = f"Your Accuracy: {yourAccuracy}%", font = (fontuse, medfont))
        if self.yourAccuracy >= self.accuracy:
            self.nextButton = tk.Button(self.frameUtility, text = "Next level",
                                    font = (fontuse, smallfont), command = self.nextLevel)
            self.nextButton.pack(side = "bottom", pady = 30)
        else:
            self.restartButton = tk.Button(self.frameUtility, text = "Restart",
                                    font = (fontuse, smallfont), command = self.restart)
            self.restartButton.pack(side = "bottom", pady = 30)
            self.loseLabel = tk.Label(self.frameUtility, text = "You lost!",
                    font = (fontuse, smallfont))
            self.loseLabel.pack(side = "bottom", pady = 10)
    
    def reset(self):
        self.canvasShowColor.destroy()
        self.frameUtility.destroy()
        del self.canvasShowColor, self.frameUtility, self.wholeframeUtility
        del self.yourAccuracy, self.accuracy
        try:
            self.nextButton.destroy()
            del self.nextButton
        except:
            self.restartButton.destroy()
            del self.restartButton
            del self.loseLabel
    
    def nextLevel(self):
        self.reset()
        self.startGame()
    
    def restart(self):
        self.reset()
        self.level = 0
        self.startGame()