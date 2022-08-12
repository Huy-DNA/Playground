import myplot
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import eval_input as evi
import numpy as np
import sys
from matplotlib.ticker import MultipleLocator

#initial setups
root = tk.Tk()
root.state("zoomed")
root.title("Graphing Calculator")
screenWidth = root.winfo_screenwidth()
root.resizable(0, 0)
framegraph = ttk.Frame(root)
leftframe = ttk.Frame(root)
framegraph.pack(side = "right", fill = "both", ipadx = screenWidth // 8)
leftframe.pack(fill = "both")
#graph setup
fig = myplot.myplot(plt.figure(), 9, 9)
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master = framegraph)
plotwidget = canvas.get_tk_widget()

limx, limy = 9, 9
xmove, ymove = None, None
def setnone():
    global xmove, ymove
    xmove, ymove = None, None
def mousedragging(event):
    global xmove, ymove, limx, limy, fig
    if xmove != None:
        limx -= event.x - xmove
        limy += event.y - ymove
        plt.clf()
        fig = myplot.myplot(fig, limx, limy)
        mainAction()
        plt.tight_layout()
        fig.canvas.draw()
    xmove, ymove = event.x, event.y
    root.after(50, setnone)
plotwidget.bind("<B1-Motion>", mousedragging)

#function
def functionGraph():
    global fig
    plt.clf()
    fig = myplot.myplot(fig, limx, limy)
    plt.plot(*(evi.eval_function(user_input.get(), limx, limy)))
    fig.canvas.draw()
def equationGraph():
    global fig
    plt.clf()
    fig = myplot.myplot(fig, limx, limy)
    plt.contour(*(evi.eval_equation(user_input.get(), limx, limy)), levels = [0])
    fig.canvas.draw()
def filledcontourGraph(*i, num = 10):
    global fig
    plt.clf()
    fig = myplot.myplot(fig, limx, limy)
    plt.contourf(*(evi.eval_equation(user_input.get(), limx, limy)), levels = num)
    plt.colorbar()
    fig.canvas.draw()
def linedcontourGraph(*i, num = 10):
    global fig
    plt.clf()
    fig = myplot.myplot(fig, limx, limy)
    plt.contour(*(evi.eval_equation(user_input.get(), limx, limy)), levels = num)
    fig.canvas.draw()
def polarGraph():
    global fig
    plt.clf()
    fig = myplot.myplot(fig, limx, limy)
    plt.plot(*(evi.eval_polar(user_input.get())))
    fig.canvas.draw()
def mainAction():
    MODE = mode.get()
    if textvar.get() == "":
        reset(soft = True)
    else:
        if MODE == 1:
            SELECTION = selection1.get()
            if SELECTION == 1:
                functionGraph()
            if SELECTION == 2:
                equationGraph()
            if SELECTION == 3:
                polarGraph()
        elif MODE == 2:
            SELECTION = selection2.get()
            if SELECTION == 1:
                filledcontourGraph(num = colornum.get())
            if SELECTION == 2:
                linedcontourGraph(num = colornum.get())
        elif MODE == 3:
            pass #for further development
def reset(*, soft = False):
    global fig, limx, limy
    plt.clf()
    if not soft: limx = limy = 9
    fig = myplot.myplot(fig, limx, limy)
    plt.tight_layout()
    fig.canvas.draw()
    textvar.set("")

#frameinput setup
frameinput = ttk.Frame(leftframe)
defaultset = ttk.Label(frameinput, text = "y =", font = ("Helvetica", 18), foreground = "blue")
textvar = tk.StringVar()
user_input = ttk.Entry(frameinput, font = ("Helvetica", 18), foreground = "blue", textvariable= textvar)
user_input.bind("<KeyRelease>", lambda event: mainAction())
user_input.focus()
frameinput.pack(fill = "both", ipady = screenWidth // 32, pady = 10, padx = 10)

#option setup
frameoption = ttk.Frame(leftframe)
selection1 = tk.IntVar()
selection1.set(1)
selection2 = tk.IntVar()
selection2.set(1)
mode = tk.IntVar()
mode.set(1)
colorLabel = ttk.Label(frameoption, text = "Number of colors used:")
colornum = tk.IntVar()
colornum.set(10)
colornumEntry = ttk.Entry(frameoption, textvariable = colornum)
colornumEntry.bind("<KeyRelease>", lambda event: mainAction())
colornumEntry.state(["disabled"])

sep = ttk.Separator(frameoption, orient = "horizontal")
sep.pack(fill = "x", padx = 5, pady = 10)

ttk.Radiobutton(frameoption,
text = "Normal graphing",
variable = mode,
value = 1,
command = lambda: [defaultset.config(text = "y ="),
                    mod2sel1.state(["disabled"]), mod2sel2.state(["disabled"]),
                    mod1sel1.state(["!disabled"]), mod1sel2.state(["!disabled"]), mod1sel3.state(["!disabled"]),
                    colornumEntry.state(["disabled"]),  textvar.set(""),
                    reset()]
).pack(expand = True, fill = "both", padx = 30, pady = 5)
mod1sel1 = ttk.Radiobutton(frameoption,
text = "Graphing function",
variable = selection1,
value = 1,
command = lambda: [defaultset.config(text = "y ="), textvar.set(""), reset()]
)

mod1sel2 = ttk.Radiobutton(frameoption,
text = "Graphing equation",
variable = selection1,
value = 2,
command = lambda: [defaultset.config(text = "0 ="), textvar.set(""), reset()]
)

mod1sel3 = ttk.Radiobutton(frameoption,
text = "Graphing using polar-coordinate system",
variable = selection1,
value = 3,
command = lambda: [defaultset.config(text = "r ="), textvar.set(""), reset()]
)

mod1sel1.pack(expand = True, fill = "both", padx = 50)
mod1sel2.pack(expand = True, fill = "both", padx = 50)
mod1sel3.pack(expand = True, fill = "both", padx = 50)

sep1 = ttk.Separator(frameoption, orient = "horizontal")
sep1.pack(fill = "x", padx = 5, pady = 10)

ttk.Radiobutton(frameoption,
text = "Graphing contour",
variable = mode,
value = 2,
command = lambda: [defaultset.config(text = "z ="),
                    mod1sel1.state(["disabled"]), mod1sel2.state(["disabled"]),
                    mod2sel1.state(["!disabled"]), mod2sel2.state(["!disabled"]), mod1sel3.state(["disabled"]),
                    textvar.set(""), colornumEntry.state(["!disabled"]), reset()]
).pack(expand = True, fill = "both", padx = 30, pady = 5)

mod2sel1 = ttk.Radiobutton(frameoption,
text = "Filled",
variable = selection2,
value = 1,
command = lambda: [textvar.set(""), reset()]
)

mod2sel2 = ttk.Radiobutton(frameoption,
text = "No Filled",
variable = selection2,
value = 2,
command = lambda: [textvar.set(""), reset()]
)

mod2sel1.pack(expand = True, fill = "both", padx = 50)
mod2sel2.pack(expand = True, fill = "both", padx = 50)

mod2sel1.state(["disabled"])
mod2sel2.state(["disabled"])

colorLabel.pack(ipady = 5, ipadx = frameoption.winfo_screenwidth() // 10)
colornumEntry.pack(padx = frameoption.winfo_screenwidth() // 24)

frameoption.pack(fill = "both")

#reset button
framebutton = ttk.Frame(leftframe)
framebutton.pack(fill = "both")
resetButton = ttk.Button(framebutton, text = "Reset", command = reset)
resetButton.pack(side = "right", padx = framebutton.winfo_screenwidth() // 24)

#Notes
notes = ttk.Labelframe(leftframe, text = "Note!")
note1 = ttk.Label(notes, text = "* For addition, subtraction, multiplication, division, exponentation, use +, -, *, /, ^.")
note2 = ttk.Label(notes, text = "* For trigonometric functions, use sin(), cos(), tan(), 1/tan().")
note3 = ttk.Label(notes, text = "* We don't accept inputs like 2x, xy, xlogx, use 2*x, x*y, x*logx.")
note4 = ttk.Label(notes, text = "* We advise against dragging when 'Graphing contour' is on.")
note1.grid(row = 0, pady = 10, sticky = "w")
note2.grid(row = 1, pady = 10, sticky = "w")
note3.grid(row = 2, pady = 10, sticky = "w")
note4.grid(row = 3, pady = 10, sticky = "w")
notes.pack(expand = True, fill = "both", padx = 10, pady = 10)
#display the widgets
defaultset.pack(fill = "both", side = "left")
user_input.pack(fill = "both", expand = True, padx = 10)
plotwidget.pack(fill = "both", expand = True)

root.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
tk.mainloop()