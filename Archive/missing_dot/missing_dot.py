import pygame
from pygame.locals import *
from info import *
import sys
from dot_setup import dotGenerator, setmode
import threading

class MissingDot():
    def __init__(self):
        pygame.init()
        self.FPS = pygame.time.Clock()
        self.gameFont()
        self.screen = pygame.display.set_mode((winWidth, winHeight))
        pygame.display.set_caption("Missing Dot")
        self.screen.fill((255, 255, 255))
        self.mainScreen()
        
    def gameFont(self):
        self.titlefont = pygame.font.SysFont(*fontitle)
        self.bigfont = pygame.font.SysFont(*fontbig)
        self.medfont = pygame.font.SysFont(*fontmed)
        self.smallfont = pygame.font.SysFont(*fontsmall)
    
    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()

                    if self.main:
                        if self.gameLabel.get_rect(left = winWidth // 2.4,
                            top = winHeight // 2.5).collidepoint(mousepos):
                                self.nextLevel()
                                self.main = False

                    if self.doneShow:
                        rect = pygame.Rect(self.leftmost + self.xdot*(self.columnspace + 10) - self.radius,
                            self.topmost + self.ydot*(self.rowspace + 10) - self.radius,
                            self.radius*2, self.radius*2)
                        if not self.lose:
                            if mousepos[1] >= 150:
                                if rect.collidepoint(mousepos):
                                    self.resetVar()
                                    self.nextLevel()
                                else:
                                    self.loseAction()
                        else:
                            if self.gameLabel.get_rect(left = winWidth // 2.4,
                                top = 10).collidepoint(mousepos):
                                    self.mainScreen()
                                    self.resetVar()
                            
                if event.type == KEYDOWN:
                    if self.lose:
                        if event.key == K_SPACE:
                            self.level = 0
                            self.lose = False
                            self.nextLevel()
            
            pygame.display.update()
            self.FPS.tick(tick)

    def mainScreen(self): #Mainscreen
        self.lose = False
        with open("highlevel.txt") as f:
            self.highlevel = f.read()
        self.screen.fill("WHITE")
        self.main = True
        self.level = 0
        self.gameName = self.titlefont.render("Missing Dot", True, "BLACK")
        self.gameLabel = pygame.image.load("missing_dot.png")
        self.screen.blit(self.gameName, (winWidth // 3, winHeight // 4))
        self.screen.blit(self.gameLabel, (winWidth // 2.4, winHeight // 2.5))
        self.screen.blit(self.smallfont.render("Click on the icon to Start game or Return to main menu", True, "BLUE"),
                        ((winWidth - 340) // 2, winHeight // 1.5) )
    def nextLevel(self): #Each level
        with open("highlevel.txt") as f:
            self.highlevel = f.read()
        self.level += 1
        self.width, self.height, (self.xdot, self.ydot), self.batches = dotGenerator(setmode(self.level))
        self.drawDotGrid()
        self.doneShow = False
        threading.Timer(1, self.dotShow).start()

    def drawDotGrid(self): #Draw blank dot grid with given size
        self.screen.fill("WHITE")
        self.displayLevel()
        self.screen.blit(self.gameLabel, (winWidth // 2.4, 10))
        self.columnspace = (winWidth - 200) // self.width
        self.rowspace = (winHeight - 200) // self.height
        self.radius = min(self.columnspace, self.rowspace) // 2
        self.leftmost = self.columnspace + 100 // self.width
        self.topmost = 100 + self.rowspace
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.circle(self.screen, "BLACK",
                radius = self.radius, width = 1,
                center = (self.leftmost + i*(self.columnspace + 10),
                        self.topmost + j*(self.rowspace + 10)))
    
    def dotShow(self, index = 0): #Show filled dots
        if index < len(self.batches):
            for (i, j) in self.batches[index]:
                pygame.draw.circle(self.screen, "BLACK", radius = self.radius, center =
                (self.leftmost + i*(self.columnspace + 10), self.topmost + j*(self.rowspace + 10)))
            threading.Timer(1, self.drawDotGrid).start()
            threading.Timer(2, lambda: self.dotShow(index + 1)).start()
        else:
            self.doneShow = True

    def displayLevel(self):
        self.screen.blit(self.medfont.render(f"Level {self.level}", True, "BLACK"),
                        (winWidth - 100, 50))
        self.screen.blit(self.medfont.render(f"Highest level: {self.highlevel}", True, "BLACK"),
                        (30, 50))

    def resetVar(self): #Cleaning
        del self.columnspace, self.rowspace, self.radius, self.leftmost, self.topmost
        del self.doneShow, self.width, self.height, self.xdot, self.ydot, self.batches

    def loseAction(self):
        self.lose = True
        self.screen.fill("WHITE")
        self.displayLevel()
        self.screen.blit(self.gameLabel, (winWidth // 2.4, 10))
        self.screen.blit(self.bigfont.render("You lost!", True, "RED"), ((winWidth + 150) // 2, 95))
        self.screen.blit(self.smallfont.render("Press Space or Click on the icon", True, "BLUE"),
                        ((winWidth + 150) // 2, 128))
        for i in range(self.width):
            for j in range(self.height):
                if i == self.xdot and j == self.ydot:
                    filled = 1
                else:
                    filled = 0
                pygame.draw.circle(self.screen, "BLACK",
                    radius = self.radius, width = filled,
                    center = (self.leftmost + i*(self.columnspace + 10),
                            self.topmost + j*(self.rowspace + 10)))    
        if self.level > int(self.highlevel):
            with open("highlevel.txt", "w") as f:
                f.write(str(self.level))

if __name__ == "__main__":
    game = MissingDot()
    game.gameLoop()