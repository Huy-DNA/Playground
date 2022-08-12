import tkinter as tk
from tkinter import ttk
import modified_widgets as mdf

mainscreen = mdf.window(main = True)
screenWidth = mainscreen.winfo_screenwidth()
midx = screenWidth // 2
hello = mdf.mylabel(mainscreen,
text = "Heeelooo!",
font = ("Times New Roman", 100),
foreground = "green"
)
hello.place(x = midx, y = 150, anchor = "center")

ask = mdf.mylabel(mainscreen,
text = "Nhập tên vào đi em yêu :3",
font = ("Times New Roman", 50),
foreground = "red"
)
ask.place(x = midx, y = 300, anchor = "center")

textvar = tk.StringVar()
entry = ttk.Entry(mainscreen, font = ("Times New Roman", 20), textvariable = textvar)
entry.place(x = midx, y = 390,
anchor = "center",
relwidth = 0.3,
relheight = 0.05,
)

button = ttk.Button(mainscreen, text = "Bắt đầu đê!", command = mainscreen.destroy)
button.place(x = midx, y = 450, anchor = "center", relheight = 0.05, relwidth = 0.05)
tk.mainloop()