# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:31:03 2023

@author: leran
"""

import pygame
import objects
from objects import Paddle
from objects import Ball
from objects import Scores

import random

pygame.init()

WIN_HEIGHT = 600
WIN_WIDTH = 900
#this is the main function, provides the UI for the game. 
color = (255,255,255)
colorText = (0,0,0)
textFont = pygame.font.SysFont("georgia", 30)
text = textFont.render('Play', True, colorText)
textWidth = text.get_width()
textHeight = text.get_height()
Rect = pygame.Rect(WIN_WIDTH/2 - textWidth, WIN_HEIGHT/2 - textHeight/2, 2*textWidth, textHeight*2)

def UI():
    run = True
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.draw.rect(win, color, Rect)
    win.blit(text, (WIN_WIDTH/2 - textWidth/2, WIN_HEIGHT/2))
    pygame.display.update()
    
    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((WIN_WIDTH/2 - textWidth <= mouse[0] <= WIN_WIDTH/2 + textWidth) 
                    and (WIN_HEIGHT/2 - textHeight <= mouse[1] <= WIN_HEIGHT/2 + textHeight)):
                    play()
                    run = False
                        
def play():
    pygame.display.quit()
    run = True
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    if random.randint(0, 1):
        yfactor = 1
    else:
        yfactor = -1
        
    if random.randint(0, 1):
        xfactor = 1
    else:
        xfactor = -1    
        
    rx = xfactor * random.uniform(1,2)
    ry = yfactor * random.uniform(1,2)
    ball = Ball(rx, ry)
    clock = pygame.time.Clock()
    scores = Scores()
    paddle1 = Paddle(50)
    paddle2 = Paddle(WIN_WIDTH-50)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        ball.move(scores)
        draw_win(win, ball, paddle1, paddle2)

def draw_win(win, ball, paddle1, paddle2):
    win.blit(objects.BG_IMG, (0,0))
    
    paddle1.draw(win)
    paddle2.draw(win)
    ball.draw(win)
    pygame.display.update()
    
UI()
pygame.display.quit()