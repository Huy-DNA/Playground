import pygame, sys
from pygame.locals import *
from entity import Buff, Food, Snake
from grid import drawGrid
from meta import winWidth, winHeight, block, tick, smallfont, bigfont, label, medfont
from playsound import playsound
import threading
import random

pygame.init()
screen = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Snake")
FPS = pygame.time.Clock()
fontbig = pygame.font.SysFont(*bigfont)
fontsmall = pygame.font.SysFont(*smallfont)
fontlabel = pygame.font.SysFont(*label)
fontmed = pygame.font.SysFont(*medfont)
snake = Snake()
lose = False
eaten = True
gamestatus = "GAME OFF"
gametick = tick
color = (255, 255, 0)
start = False
score = 0
#sound = threading.Thread(target = lambda: playsound("ScheiBe.mp3"), daemon = True)
#sound.start()
while True:
    if not start:
        with open("highscore.txt") as f:
            highscore = f.read()
        screen.blit(fontsmall.render("Press Space to start", True, (0, 255, 0)),
        (block*8.2, block*3.8))
    screen.fill("BLACK")
    screen.blit(fontbig.render(gamestatus, True, color), 
    ((winWidth - len(gamestatus) * 17) // 2, block * 2))
    screen.blit(fontmed.render("Score: ", True, "WHITE"),
    (30, block * 0.5))
    screen.blit(fontmed.render("High score: ", True, "WHITE"),
    (winWidth - 200, block * 0.5))
    screen.blit(fontmed.render(highscore, True, "WHITE"),
    (winWidth - 100, block * 0.5))
    screen.blit(fontmed.render(str(score), True, "WHITE"),
    (85, block * 0.5))
    if not lose and start:
        if eaten:
            food = Food(snake.xlist, snake.ylist)
            reverse = random.choice([False] * 5 + [True])
            eaten = False
        if reverse:
            pygame.draw.rect(screen, (200, 255, 200), food.rect)
            screen.blit(fontlabel.render("R", True, (0,0,0)), (food.rect.left + block // 4, food.rect.top))
        else:
            pygame.draw.rect(screen, (0, 255, 0), food.rect)
        for partnum in range(len(snake.list)):
            if partnum != 0:
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(*snake.list[partnum]))
            else:
                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect(*snake.list[partnum]))
        snake.moveWhole()
        if snake.collideSelf():
            lose = True
        if snake.collideFood(food.xfood, food.yfood, reverse):
            eaten = True
            score += 200
            if reverse:
                score += 200
            if gametick < 20:
                gametick += 0.5
    drawGrid(screen)
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    snake.setDirection(-1)
                elif event.key == K_RIGHT:
                    snake.setDirection(1)
                elif event.key == K_UP:
                    snake.setDirection(2)
                elif event.key == K_DOWN:
                    snake.setDirection(-2)
                elif event.key == K_SPACE:
                    start = True
                    gamestatus = "GAME ON"
                    color = (0, 255, 0)
    if lose:
        gamestatus = "GAME OVER"
        color = (255, 0, 0)
        start = False
        lose = False
        gametick = tick
        snake = Snake()
        if score > int(highscore):
            with open("highscore.txt", "w") as f:
                f.write(str(score))
        score = 0
    pygame.display.update()
    FPS.tick(gametick)