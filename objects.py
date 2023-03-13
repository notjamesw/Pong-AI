# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:35:23 2023

@author: leran
"""
import pygame
import os


WIN_HEIGHT = 600
WIN_WIDTH = 900
BG_IMG = pygame.image.load(os.path.join("images","PONG_bg.png"))
PADDLE_IMG = pygame.image.load(os.path.join("images", "PONG_paddle.png"))
BALL_IMG = pygame.image.load(os.path.join("images", "PONG_ball.png"))

class Scores:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        
class Paddle:
    img = PADDLE_IMG
    length = img.get_height()
    width = img.get_width()
    vel = 2
    def __init__(self, x):
        self.y = WIN_HEIGHT/2 - self.length/2
        self.x = x
    
    def move(self, direction):
        if direction:
            if self.y - self.vel >= 0:
                self.y -= self.vel
            else:
                self.y = 0
        else:
            if self.y + self.vel <= WIN_HEIGHT - self.length:
                self.y += self.vel
            else:
                self.y = WIN_HEIGHT - self.length
    
    def collide(self, ball):
        ball_mask = ball.get_mask()
        paddle_mask = self.get_mask()
        
        offset = (self.x - ball.x, self.y - round(ball.y))
        
        overlap = ball_mask.overlap(paddle_mask, offset)
        
        if overlap:
            self.yvel = self.yvel * -1
            self.xvel = self.xvel * -1
            
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        
class Ball:
    img = BALL_IMG
    height = img.get_height()
    width = img.get_width()
    
    def __init__(self, xvel, yvel):
        self.xvel = xvel
        self.yvel = yvel
        self.x  = WIN_WIDTH/2
        self.y = WIN_HEIGHT/2
    
    def collide(self):
        self.yvel = self.yvel * -1
        print(self.yvel)
    
    def score(self, scores):
        if self.x <= 0:
            scores.player1 += 1
            return True
        elif self.x >= WIN_WIDTH - self.width:
            scores.player2 += 1
            return True
        else:
            return False
        
    def move(self, scores):
        if self.yvel < 0:
            if self.y + self.yvel > 0:
                self.y += self.yvel 
            else:
                self.y == 0
                self.collide()
        else:
            if self.y + self.yvel < WIN_HEIGHT - self.height:
                self.y += self.yvel
            else:
                self.y == WIN_HEIGHT - self.height
                self.collide()
                
        if self.x + self.xvel >= 0 and self.x + self.xvel <= WIN_WIDTH - self.width:
            self.x += self.xvel 
        else:
            if self.xvel < 0:
                self.x == 0
            else: 
                self.x == WIN_WIDTH - self.width
        
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))