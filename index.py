#from Game import Game
#from Paquet import Paquet
import pygame, sys
pygame.init()

size = width, height = 1280, 720
bgColor = 255, 255, 255
launchButtonColor = 138, 43, 226

pygame.display.set_caption("Jeu du Barbu")
icon = pygame.image.load("src/icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)

"""paquet = Paquet()
paquet.battre()

card = paquet.tirer()
cardRect = card.aff.get_rect()

cardRect.move_ip(width//2, height//2)"""

font = pygame.font.Font("src/KGRedHands.ttf", 128)
widthText, heightText = font.size("LAUNCH")
launchTxt = font.render("LAUNCH", True, (0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(bgColor)
    screen.blit(launchTxt, (width//2 - widthText//2, height//2 - heightText//2))
    #screen.blit(card.aff, cardRect)
    pygame.display.update()