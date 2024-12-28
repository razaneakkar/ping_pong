import pygame
import random
pygame.init()

WIDTH = 900
HEIGHT = 600
FPS = 60
black = (0, 0, 0)
white = (255, 255,255)

screen = pygame.display.set_mode (WIDTH,HEIGHT) 
pygame.display.set_caption("ping pong")

ball_raduis = 10

class pong