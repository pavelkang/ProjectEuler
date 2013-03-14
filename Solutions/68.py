from pygame import *
import pygame
pygame.init()
def isP(x):
    if x == 1:
        return False
    elif x ==2:
        return True
    else:
        for i in xrange(3,int(x**0.5)+1):
            if x%i == 0:
                return False
    return True
print '1'

sound = pygame.mixer.Sound('Power Up.wav')
sound.play()

pygame.mixer.music.load('Power Up.wav')
pygame.mixer.music.play(1,0.0)
