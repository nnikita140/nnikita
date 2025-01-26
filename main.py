import pygame
import sys
from random import randint

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (1100,900))
bg_width, bg_height = bg.get_size()


pygame.display.set_caption('Платформер')

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)



y_speed = 0
gravity = 0.5
jump_strength = -10
on_ground = True




platforms = [(0, bg_height, bg_wodth, 10),
             (600,700,100,10),
             (700,800,100,10),
             (400,700,100,10),
             (300,600,100,10),
             (200, 500, 100, 10),
             (400, 400, 150, 10),
             (220, 300, 70, 10),
             (370,200,100,10),
             (490,100,100,10)]
player = pygame.transform,scale(pygame.image.load('cat.png'), (70,70))
player_rect = player.get_rect()
player_rect.x = 100
player_rect.y = 150


pizza = pygame.transform.scale(pygame.image.load('pizza.png'), (70,70))
pizza_rect = pizza.get_rect()
pizza_rect.x = 530
pizza_rect.y = 30


mouse = pygame.transform.scale(pygame.image.load('mouse.png'), (70,70))
mouses = []
for _ in range(5):
    