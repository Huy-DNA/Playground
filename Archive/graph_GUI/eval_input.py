import numpy as np
import re
import matplotlib.pyplot as plt

def eval_function(string_input, limx, limy):
    string_input.lower()
    string_input = re.sub("\^", "**", string_input)
    x = np.linspace(limx - 18, limx, 1000)
    try:
        y = eval(string_input, globals(), {"cos": np.cos, "sin" : np.sin, "tan": np.tan, "log": np.log10, "ln": np.log, "x" : x, "e" : np.e})
        if isinstance(y, int):
            y = np.full(1000, y)
    except:
        return (0, 0)
    return (x, y)
def eval_equation(string_input, limx, limy):
    string_input.lower()
    string_input = re.sub("\^", "**", string_input)
    x = np.linspace(limx - 18, limx, 1000)
    y = np.linspace(limy - 18, limy, 1000)
    x, y = np.meshgrid(x, y)
    try:
        z = eval(string_input, globals(), {"cos": np.cos, "sin" : np.sin, "tan": np.tan, "log": np.log10, "ln": np.log, "x" : x, "y": y, "e": np.e})
    except:
        return ([[0, 0]], [[0, 0]], [[0, 0]])
    return (x, y, z)
def eval_polar(string_input):
    string_input.lower()
    string_input = re.sub("\^", "**", string_input)
    phi = np.linspace(-200, 200, 10000)
    try:
        r = eval(string_input, globals(), {"cos": np.cos, "sin" : np.sin, "tan": np.tan, "log": np.log10, "ln": np.log, "phi" : phi, "e" : np.e})
        if isinstance(r, int):
            r = np.full(1000, r)
    except:
        return (0, 0)
    return (r * np.cos(phi), r * np.sin(phi))