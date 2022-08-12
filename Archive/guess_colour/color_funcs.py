import numpy as np

def colorCompare(myrgb, yourrgb):
    myr, myg, myb = myrgb
    yourr, yourg, yourb = yourrgb
    meanr = (myr + yourr) / 2
    deltar = (myr - yourr) ** 2
    deltag = (myg - yourg) ** 2
    deltab = (myb - yourb) ** 2
    deltaC = np.sqrt((2 + meanr/256) * deltar + 4 * deltag + (2 + (255 - meanr)/256) * deltab)
    return abs(round((1 - deltaC / 256) * 100))

def color_to_hex(rgb: tuple):
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"
