# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:35:23 2023

@author: leran
"""
import pygame
import os
import random

WIN_HEIGHT = 600
WIN_WIDTH = 900
BG_IMG = pygame.image.load(os.path.join("images","PONG_bg.png"))
PADDLE_IMG = pygame.image.load(os.path.join("images", "PONG_paddle.png"))
BALL_IMG = pygame.image.load(os.path.join("images", "PONG_ball.png"))
colorText = (0,0,0)

pygame.init()

#represents a scoreboard
class Scores:
    textFont = pygame.font.SysFont("georgia", 14)
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        
    def draw(self, win):
        textScoreP1 = self.textFont.render(f"{self.player1}", False, colorText)
        textScoreP2 = self.textFont.render(f"{self.player2}", False, colorText)
        win.blit(textScoreP2, (WIN_WIDTH/2 - 20, WIN_HEIGHT/2))
        win.blit(textScoreP1, (WIN_WIDTH/2 + 10, WIN_HEIGHT/2))

#represents a paddle board, can only move up and down
class Paddle:
    img = PADDLE_IMG
    length = img.get_height()
    width = img.get_width()
    vel = 5
    def __init__(self, x):
        self.y = WIN_HEIGHT/2 - self.length/2
        self.x = x
        self.rect = self.img.get_rect(topleft = (self.x, self.y))
    
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
        self.rect.x = self.x
        self.rect.y = self.y
        
    def collide(self, ball):
        diff = self.y - ball.y + self.length/2
            
        if self.rect.colliderect(ball.rect):
            ball.xvel = ball.xvel * -1 
            if abs(ball.xvel) < 10:
                if ball.xvel < 0:
                    ball.xvel -= random.uniform(0,1)
                else:
                    ball.xvel += random.uniform(0,1)
                if diff * ball.yvel < 0 and abs(diff) > ball.height/2:
                    ball.yvel *= -1;
                
            
    def draw(self, win):
        win.blit(self.img, self.rect)

#represents a ball that bounces off top and bottom wall
class Ball:
    img = BALL_IMG
    height = img.get_height()
    width = img.get_width()
    
    def __init__(self, xvel, yvel):
        self.xvel = xvel
        self.yvel = yvel
        self.x  = WIN_WIDTH/2
        self.y = WIN_HEIGHT/2
        self.rect = self.img.get_rect(topleft = (self.x, self.y))
    
    def collide(self):
        self.yvel *= -1
    
    def score(self, scores):
        if self.x == 0:
            scores.player1 += 1
            return True
        elif self.x == WIN_WIDTH - self.width:
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
                
        if self.x + self.xvel > 0 and self.x + self.xvel < WIN_WIDTH - self.width:
            self.x += self.xvel 
        else:
            if self.xvel < 0:
                self.x = 0
            else: 
                self.x = WIN_WIDTH - self.width
                
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self, win):
        win.blit(self.img, self.rect)
        
        