import pygame
from pygame.locals import *
from meta import winHeight, winWidth, block, playground, grid
import random

class Snake():
    def __init__(self):
        self.list = []
        self.xlist = []
        self.ylist = []
        self.isgrow = False
        self.length = 5
        for i in range(self.length):
            self.list.append((winWidth + block*(i-5), playground, block, block))
            self.xlist.append(winWidth + block*(i-5))
            self.ylist.append(playground)
        self.direction = -1 #left
    def moveWhole(self):
        if self.isgrow:
            self.grow()
            self.isgrow = False
        for i in range(self.length - 1, 0, -1):
            self.list[i] = self.list[i - 1]
        self.xlist.pop(-1)
        self.ylist.pop(-1)
        self.list[0] = self.moveHead(self.list[0])
        self.xlist.insert(0, self.list[0][0])
        self.ylist.insert(0, self.list[0][1])
    def setDirection(self, direction, reverse = False):
        if reverse == True or (
        self.direction != direction and self.direction != -direction
        ):
            self.direction = direction
    def moveHead(self, head):
        left, top, *_ = head
        if self.direction == -1: #left
            if left >= block:
                head = (left - block, top, block, block)
            else:
                head = (winWidth - block, top, block, block)
        elif self.direction == 1: #right
            if left <= winWidth - block*2:
                head = (left + block, top, block, block)
            else:
                head = (0, top, block, block)
        elif self.direction == 2: #up
            if top >= playground + block:
                head = (left, top - block, block, block)
            else:
                head = (left, winHeight - block, block, block)
        else: #down
            if top <= winHeight - block * 2:
                head = (left, top + block, block, block)
            else:
                head = (left, playground, block, block)
        return head
    def grow(self):
        self.list.append(self.list[self.length - 1])
        self.xlist.append(self.list[self.length - 1][0])
        self.ylist.append(self.list[self.length - 1][1])
        self.length += 1
    def collideSelf(self):
        left, top, *_ = self.list[0]
        for i in range(1, self.length):
            if left == self.list[i][0] and top == self.list[i][1]:
                return True
    def collideFood(self, x, y, reverse):
        left, top, *_ = self.list[0]
        if left == x and top == y:
            self.isgrow = True
            if reverse:
                self.collideReverse()
            return True
    def collideReverse(self):
        self.list = self.list[::-1]
        left, top, *_ = self.list[0]
        left1, top1, *_ = self.list[1]
        if top == top1:
            if left > left1:
                self.setDirection(1, True)
            elif left < left1:
                self.setDirection(-1, True)
        elif top > top1:
            self.setDirection(-2, True)
        elif top < top1:
            self.setDirection(2, True)
class Food():
    def __init__(self, xlist, ylist):
        poslist = list(zip(xlist, ylist))
        randompos = random.choice([i for i in grid if i not in poslist])
        self.xfood, self.yfood = randompos
        self.rect = pygame.Rect(self.xfood, self.yfood, block, block)
class Buff(Food):
    def __init__(self, xlist, ylist, xfood, yfood):
        super().__init__(xlist + xfood, ylist + yfood)
        self.type = random.choice(["Short", "Slow"] + [None] * 10)