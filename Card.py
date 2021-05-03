from random import shuffle 

# la liste des images de cartes (sans les cavaliers)
jeu_image = [chr(x) for x in (list(range(0x1f0a1, 0x1f0af))
                         + list(range(0x1f0b1, 0x1f0bf))
                         + list(range(0x1f0c1, 0x1f0cf))
                         + list(range(0x1f0d1, 0x1f0df))) if x not in [0x1f0ac,0x1f0bc,0x1f0cc,0x1f0dc]]
   
"""Ouais ouais ouais"""

class Card():
    "Définition d'une carte"
    
    def __init__(self,val='as',coul='carreau',n=0): # le constructeur
        self.value = val
        self.couleur = coul
        self.num=n
        if self.couleur == 'pique':
            self.aff = jeu_image[self.num]
        if self.couleur == 'coeur':
            self.aff = jeu_image[self.num + 13]
        if self.couleur == 'carreau':
            self.aff = jeu_image[self.num + 26]
        if self.couleur == 'trèfle':
            self.aff = jeu_image[self.num + 39]
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