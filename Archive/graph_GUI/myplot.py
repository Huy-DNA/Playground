import matplotlib
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator

def myplot(fig, limx, limy):
    sub = fig.add_subplot()
    sub.set_aspect("equal")
    sub.set_xlim([limx - 18, limx])
    sub.set_ylim([limy - 18, limy])
    sub.spines[["top", "right"]].set_visible(False)
    sub.grid(axis = "both", which = "both")
    sub.xaxis.set_minor_locator(MultipleLocator(1))
    sub.yaxis.set_minor_locator(MultipleLocator(1))
    if 0 <= limx <= 18:
        sub.spines["left"].set_position("zero")
    else:
        sub.spines["left"].set_visible(False)
        #if limx < 0:
        #    sub.tick_params(right = "on", labelright = "on")
        #else:
        #    sub.tick_params(left = "on", labelleft = "on")
    if 0 <= limy <= 18:
        sub.spines["bottom"].set_position("zero")
    else:
        sub.spines["bottom"].set_visible(False)
        #if limy < 0:
        #    sub.tick_params(top = "on", labeltop = "on", bottom = "off", labelbottom = "off")
        #else:
        #    sub.tick_params(bottom = "on", labelbottom = "on")
    return fig