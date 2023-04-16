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
textPlay = textFont.render('Play', True, colorText)
textPause = textFont.render('Game Paused, to unpause, press escape',
                            True, colorText)
textWidthPlay = textPlay.get_width()
textHeightPlay = textPlay.get_height()
textWidthPause = textPause.get_width()
textHeightPause = textPause.get_height()

Rect = pygame.Rect(WIN_WIDTH/2 - textWidthPlay, WIN_HEIGHT/2 - textHeightPlay/2
                   , 2*textWidthPlay, textHeightPlay*2)
Rect2 = pygame.Rect(WIN_WIDTH, WIN_HEIGHT, 2*textWidthPause, textHeightPause*2)

#represents the main window and game start screen
def UI():
    run = True
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.draw.rect(win, color, Rect)
    win.blit(textPlay, (WIN_WIDTH/2 - textWidthPlay/2, WIN_HEIGHT/2))
    pygame.display.update()
    
    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((WIN_WIDTH/2 - textWidthPlay <= mouse[0] 
                     <= WIN_WIDTH/2 + textWidthPlay) 
                    and (WIN_HEIGHT/2 - textHeightPlay <= mouse[1] 
                         <= WIN_HEIGHT/2 + textHeightPlay)):
                    play()
                    run = False

#represents the main game, takes in inputs from the keyboard 
def play():
    pygame.display.quit()
    run = True
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    scores = Scores()
    paddle1 = Paddle(20)
    paddle2 = Paddle(WIN_WIDTH-20 - paddle1.width)
    ball = round()
    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle2.move(1)
        if keys[pygame.K_DOWN]:
            paddle2.move(0)
        if keys[pygame.K_w]:
            paddle1.move(1)
        if keys[pygame.K_s]:
            paddle1.move(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif (event.type == pygame.KEYDOWN 
                  and event.key == pygame.K_ESCAPE):
                if (pauseGame(win)):
                    run = False
                    
        ball.move(scores)
        paddle1.collide(ball)
        paddle2.collide(ball)
        if ball.score(scores):
            ball = round()

        draw_win(win, ball, paddle1, paddle2, scores)

#creates a new ball for each new round at the starting position
def round():
    if random.randint(0, 1):
        yfactor = 1
    else:
        yfactor = -1
        
    if random.randint(0, 1):
        xfactor = 1
    else:
        xfactor = -1    
        
    rx = xfactor * random.uniform(3,4)
    ry = yfactor * random.uniform(3,4)
    ball = Ball(rx, ry)
    return ball;

#draw/renders the images on to the screen
def draw_win(win, ball, paddle1, paddle2, scores):
    win.blit(objects.BG_IMG, (0,0))
    
    paddle1.draw(win)
    paddle2.draw(win)
    ball.draw(win)
    scores.draw(win)
    pygame.display.update()

#calls when esc is pressed, pauses the game
def pauseGame(win):
    pygame.draw.rect(win, (255, 255, 255), Rect2)
    win.blit(textPause, (WIN_WIDTH/2 - textWidthPause/2, WIN_HEIGHT/2))
    pygame.display.update()
    pause = True
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif (event.type == pygame.KEYDOWN 
                  and event.key == pygame.K_ESCAPE):
                return False
    
UI()
pygame.display.quit()