import random

def dotGenerator(mode):
    if mode == "easy":
        size = random.choice([(4, 4, 5), (5, 3, 7)])
    elif mode == "intermediate":
        size = random.choice([(5, 5, 6), (7, 4, 9), (9, 3, 13)])
    elif mode == "hard":
        size = random.choice([(10, 4, None), (9, 5, None), (8, 6, None)])
    
    width, height, num = size
    xdot = random.randrange(width)
    ydot = random.randrange(height)
    filled = [(i, j) for i in range(width) for j in range(height) 
                    if i != xdot or j != ydot]
    if mode != "hard":
        batches = [ [filled.pop(random.randrange(len(filled))) for i in range(num)]
                    for i in range((width * height - 1) // num)]
    else:
        batches = []
        while len(filled) > 0:
            try:
                num = random.randrange( len(filled) - 1 ) + 2
            except:
                num = 1
            batches.append( [filled.pop(random.randrange(len(filled))) for i in range(num)] )
    return width, height, (xdot, ydot), batches

def setmode(level):
    if level <= 3:
        return "easy"
    elif level <= 6:
        return "intermediate"
    else:
        return random.choice(["intermediate", "hard"])

if __name__ == "__main__":
    print(dotGenerator(setmode(level = 10)))