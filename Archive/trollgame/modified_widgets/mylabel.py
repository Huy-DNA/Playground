from tkinter import ttk

class mylabel(ttk.Label):
    def __init__(self, master, *, text = "", font = (), foreground = ""):
        super().__init__(master, background = "#B0E0E6", text = text, font = font, foreground = foreground)