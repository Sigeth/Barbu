from pygame.constants import RESIZABLE
from Player import Player

from Paquet import Paquet

from random import choice, randint

import pygame, sys

class Game():


    def __init__(self, nbPlayers=4, nbCards=52):

        pygame.init()

        self.nbPlayers = nbPlayers

        self.nbCards = nbCards

        self.paquet = Paquet()

        self.players = [Player("Player " + str(i+1)) for i in range(nbPlayers)]

        self.currentContract = None

        self.playerToPick = choice(self.players)

        self.trickNb = None

        self.roundNb = len(self.players[0].contractList)

        self.currentState = "WaitingScreen"

        self.size = self.width, self.height = 1280, 720

        self.bgColor = 0, 128, 0

        pygame.display.set_caption("Jeu du Barbu")
        icon = pygame.image.load("src/icon.png")
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode(self.size, RESIZABLE)

        self.fontSrc = "src/KGRedHands.ttf"
        self.fontSize = 96

        self.launchScreen()
    

    def launchScreen(self):
        """
        Affiche l'écran d'acceuil et le bouton LAUNCH au lancement.
        """
        self.paquet.battre()

        font = pygame.font.Font(self.fontSrc, self.fontSize)
        widthText, heightText = font.size("LAUNCH")

        delayms = 1000
        currentDelay = 1000
        cardsToDisplay = [None for i in range(6)]
        while self.currentState == "WaitingScreen":
            mouseX, mouseY = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            self.screen.fill(self.bgColor)

            if currentDelay >= delayms:
                for i in range(6):
                    card = choice(self.paquet.cartes)
                    cardRect = card.aff.get_rect()
                    widthCard, heightCard = (0, 0)
                    if i == 0 or i == 3:
                        widthCard = 50
                    elif i == 1 or i == 4:
                        widthCard = self.width//2 - 192//2
                    else:
                        widthCard = self.width - 50 - 192
                    
                    if i < 3:
                        heightCard = 0
                    else:
                        heightCard = self.height - 290
                    
                    cardRect.move_ip(widthCard, heightCard)
                    cardsToDisplay[i] = (card.aff, cardRect)
                currentDelay = 0

            for card, cardRect in cardsToDisplay:
                self.screen.blit(card, cardRect)

            colorText = (0, 0, 0)
            if (self.width//2 - widthText//2 < mouseX and mouseX < self.width//2 + widthText//2) and (self.height//2 - heightText//2 < mouseY and mouseY < self.height//2 + heightText//2):
                colorText = (randint(0, 255), randint(0, 255), randint(0, 255))
                if pygame.mouse.get_pressed(3)[0]:
                    self.currentState = "launch?"
                    self.launch()

            launchTxt = font.render("LAUNCH", True, colorText)
            self.screen.blit(launchTxt, (self.width//2 - widthText//2, self.height//2 - heightText//2))
            pygame.display.update()
            currentDelay += 1
        
    
    def draw(self):
        """
        Distribue les cartes.
        """

        self.clearDecks()

        self.paquet.battre()

        for i in range(self.nbCards//self.nbPlayers):

            for p in self.players:

                p.take(self.paquet.tirer())


    def launch(self):
        """
        Affiche le choix des noms.
        """
        self.screen.fill(self.bgColor)

        pygame.display.update()

        self.fontSize = 48

        font = pygame.font.Font(self.fontSrc, self.fontSize)

        for p in self.players:

            name = p.setName(self.screen, self.bgColor, font, self.width, self.height, self.players)

            print(name)

        self.currentState = "GameState"

        #self.endScreen()

        self.gameState()
    
    def playerWaitingScreen(self, p, font):
        ready = False

        while not ready:
            self.screen = p.waitingScreen(self.screen, self.bgColor, font, self.width, self.height)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        ready = True
            
            pygame.display.update()

    def endScreen(self):
        """
        Affiche les gagnants de la partie ainsi qu'un classement des joueurs (et un trophée)
        """

        self.currentState = "endScreen"
        image = pygame.image.load('src/images/trophy.png')
        rectangle = image.get_rect()
        rectangle.center = (100,100)
        rectangle.inflate_ip(-50,-50)
        winnerFont = pygame.font.Font(self.fontSrc, self.fontSize)
        font = pygame.font.Font(self.fontSrc, self.fontSize//2)
        #widthText, heightText = font.size("LAUNCH")
        winnertext = "Les gagnants sont : " + "\n".join([p.name for p in self.findWinners()])
        textsurface = winnerFont.render(winnertext, False, (0, 0, 0))
        sorted_players = self.players.sort(key=self.get_rank_key)
        ranking_text = "Voici le classement : " + "\n".join([p.name for p in sorted_players])
        
        
        while self.currentState == "endScreen":
            #rectangle.show()
            mouseX, mouseY = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            self.screen.fill(self.bgColor)
            self.screen.blit(image, rectangle)
            self.screen.blit(textsurface,(0,0))
            
            pygame.display.update() 

            


    def clearDecks(self):
        """
        Vide les decks.
        """
        for p in self.players:

            for card in p.deck:
                self.paquet.remettre(card)
            
            p.deck = []

    def trick(self, firstPlayer: Player, roundId: int) -> Player:
        """
        Effectue un tour de jeu.
        """
        deckThrow = []

        index = self.players.index(firstPlayer)

        font = pygame.font.Font(self.fontSrc, self.fontSize)

        for j in range(len(self.players)):

            player = self.players[(index + j) % 4]

            chosing = True
            while chosing:
                mouseX, mouseY = pygame.mouse.get_pos()
                
                self.screen, cards = firstPlayer.showCards(self.screen, self.bgColor, font, self.width, self.height)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mouseY >= self.height - 285:
                            i = mouseX // (self.width//len(firstPlayer.deck)) 
                            if cards[i].collidepoint(mouseX, mouseY):
                                card = player.chooseCardTrick(deckThrow, i)
                                deckThrow.append((card, player))
                                chosing = False
                                print((card.value, card.couleur))
                                break

                pygame.display.update()

        for card in [tupl[0] for tupl in deckThrow]:

            self.paquet.remettre(card)
            
        return self.calculatePoints(deckThrow,roundId)


    def calculatePoints(self, deckThrow: tuple, roundId: int) -> Player:
        """
        Définie le joueur qui gagne le trick et lui donne ces points.
        """

        trickColor= deckThrow[0][0].couleur

        winnerCard= deckThrow[0]

        for el in deckThrow:

            if el[0].couleur==trickColor and el[0].point>winnerCard[0].point:

                    winnerCard=el

        winner=winnerCard

        winner[1].addPoints(10)

        for el in deckThrow:

            card = el[0]

            if (card.value == "roi" and card.couleur == "coeur") and (self.currentContract["name"] == "Roi barbu" or self.currentContract["name"] == "Salade"):

                winner[1].addPoints(100)

            elif (card.value == "dame") and (self.currentContract["name"] == "Dames" or self.currentContract["name"] == "Salade"):

                winner[1].addPoints(25)

            if (card.couleur == "coeur") and (self.currentContract["name"] == "Coeurs" or self.currentContract["name"] == "Salade"):

                winner[1].addPoints(10)

        points = sorted([p.points for p in self.players])

        for p in self.players:

            p.rank=points.index(p.points)+1

        return winner[1]
        

    def checkVictory(self) -> bool:
        """
        Test si le contrat actuel est terminé ou non.
        """
        victory = False

        for player in self.players:

            for card in player.deck:

                if self.currentContract["name"] == "Roi barbu" and (card.value == "roi" and card.couleur == "coeur"):

                    victory = True

                elif self.currentContract["name"] == "Dames" and card.value == "dame":

                    victory = True

                elif self.currentContract["name"] == "Coeurs" and card.couleur == "coeur":

                    victory = True
                    
                elif self.currentContract["name"] == "Salade" and ((card.value == "dame") or (card.couleur == "coeur")):
                    
                    victory = True

        return victory
        
    def round(self):
        """
        Lance les tricks et les test.
        """
        roundId = 0

        firstPlayer=self.playerToPick

        while roundId <= self.trickNb and self.checkVictory():

            roundId+=1

            firstPlayer = self.trick(firstPlayer, roundId)

            print(([p.points for p in self.players]))
            print(([p.rank for p in self.players]))
    
    def gameState(self):
        """
        Lance les rounds, affiche les contrats et calcule le vainqueur.
        """
        for i in range(len(self.players[0].contractList)//2*len(self.players)):

            self.draw()

            self.trickNb = len(self.players[0].deck)

            font = pygame.font.Font(self.fontSrc, self.fontSize)

            self.playerWaitingScreen(self.playerToPick, font)

            chosing = True

            while chosing:
                mouseX, mouseY = pygame.mouse.get_pos()
                
                self.screen, cards = self.playerToPick.showCards(self.screen, self.bgColor, font, self.width, self.height)

                transparentRect = pygame.Surface(self.size, pygame.SRCALPHA)
                transparentRect.fill((0,0,0,176))
                self.screen.blit(transparentRect, (0,0))

                self.screen, contracts = self.playerToPick.showContracts(self.screen, self.bgColor, font, self.width, self.height)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mouseY >= self.height//2 - 280//2 and mouseY <= self.height//2 + 280//2:
                            i = (mouseX - 192//2) // (self.width//len(self.playerToPick.contractList)) 
                            if contracts[i].collidepoint(mouseX, mouseY):
                                self.currentContract = self.playerToPick.chooseContract(i)
                                print(self.currentContract["name"])
                                chosing = False
                
                pygame.display.update()

            
            self.round()

            if self.players[-1]==self.playerToPick:

                self.playerToPick=self.players[0]

            else:

                self.playerToPick=self.players[self.players.index(self.playerToPick)+1]

        self.endScreen()
        
    def findWinners(self):

        i=self.players[0].points

        win=[]

        for player in self.players:

            if player.points<i:

                i=player.points

                win=[player]

            elif player.points==i:

                win.append(player)

        return win

    def get_rank_key(p):
        return p['rank']