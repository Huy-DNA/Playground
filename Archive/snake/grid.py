import pygame
from meta import winWidth, winHeight, block

def drawGrid(screen):
    for x in range(0, winWidth, block):
        for y in range(0, winHeight, block):
            rect = pygame.Rect(x, y + block * 5, block, block)
            pygame.draw.rect(screen, "BLUE", rect, 1)
