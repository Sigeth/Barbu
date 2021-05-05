from random import shuffle
import pygame

class Card():
    "Définition d'une carte"
    
    def __init__(self,val='as',coul='carreau',n=0): # le constructeur
        self.value = val
        self.couleur = coul
        self.num=n
        if self.couleur == 'pique':
            self.aff = pygame.image.load("src/cards/" + str(n) + ".png")
        if self.couleur == 'trèfle':
            self.aff = pygame.image.load("src/cards/" + str(n+13) + ".png")
        if self.couleur == 'carreau':
            self.aff = pygame.image.load("src/cards/" + str(n+26) + ".png")
        if self.couleur == 'coeur':
            self.aff = pygame.image.load("src/cards/" + str(n+39) + ".png")
        if self.value == "as":
            self.point = 14
        if self.value == "valet":
            self.point = 11
        if self.value == "dame":
            self.point = 12
        if self.value == "roi":
            self.point = 13
        if self.value in ('2','3','4','5','6','7','8','9','10'):
            self.point = int(self.value)