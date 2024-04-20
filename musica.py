import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load('shapeofyou.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)

