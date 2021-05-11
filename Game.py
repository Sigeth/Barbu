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

        self.trickNb = len(self.players[0].deck)

        self.roundNb = len(self.players[0].contracts)

        self.currentState = "WaitingScreen"

        self.size = self.width, self.height = 1280, 720

        self.bgColor = 255, 255, 255

        pygame.display.set_caption("Jeu du Barbu")
        icon = pygame.image.load("src/icon.png")
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode(self.size)

        self.fontSrc = "src/KGRedHands.ttf"
        self.fontSize = 96

        self.waitingScreen()
    

    def waitingScreen(self):
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


    def launch(self):

        self.screen.fill(self.bgColor)

        pygame.display.update()

        self.fontSize = 48

        font = pygame.font.Font(self.fontSrc, self.fontSize)
        
        x = 20

        for p in self.players:

            name = p.setName(self.screen, font, self.width, self.height, self.players)



            print(name)

        self.changeContract(self.playerToPick)

        self.round()


    def draw(self):

        self.clearDecks()

        self.paquet.battre()

        for i in range(self.nbCards//self.nbPlayers):

            for p in self.players:

                p.take(self.paquet.tirer())
            

    def clearDecks(self):

        for p in self.players:

            p.deck = []
        


    def changeContract(self, p):

        self.currentContract = p.chooseContract()


    def trick(self, firstPlayer,roundId):

        deckThrow = []

        index = self.players.index(firstPlayer)

        for i in range(len(self.players)):

            player = self.players[index + i - (4*((index+i)//4))]

            card = player.chooseCardTrick(deckThrow)

            deckThrow.append((card,player))

        return self.calculatePoints(deckThrow,roundId)



    def calculatePoints(self, deckThrow, roundId):
        """
        @param deckThrow: tuple that contains tuples where first element is the card and the second is the player linked (card, linkedPlayer)
        """

        trickColor= deckThrow[0][0].couleur

        winnerCard= deckThrow[0]

        for el in deckThrow:

            if el[0].couleur==trickColor and el[0].point>winnerCard[0].point:

                    winnerCard=el

        winner=winnerCard

        if self.currentContract == "Pli" or self.currentContract == "Salade":

            winner[1].addPoints(10)

        if self.currentContract == "Dernier pli" or self.currentContract == "Salade" and roundId==13:

            winner[1].addPoints(100)

        if self.currentContract != "Pli" or self.currentContract != "Dernier pli":

            for el in deckThrow:

                card = el[0]

                if (card.value == "roi" and card.couleur == "coeur") and (self.currentContract == "Roi Barbu" or self.currentContract == "Salade"):

                    winner[1].addPoints(100)

                elif (card.value == "dame") and (self.currentContract == "Dames" or self.currentContract == "Salade"):

                    winner[1].addPoints(25)

                if (card.couleur == "coeur") and (self.currentContract == "Coeurs" or self.currentContract == "Salade"):

                    winner[1].addPoints(10)
        
        return winner[1]
        

    def checkVictory(self):

        for player in self.players:

            for card in player.deck:

                if self.currentContract == "Roi Barbu" and (card.value == "roi" and card.couleur == "coeur"):

                    return True

                elif self.currentContract == "Dames" and card.value == "dame":

                    return True

                elif self.currentContract == "Coeurs" and card.couleur == "coeur":

                    return True

        return False
        
    def round(self):

        roundId = 0

        self.draw()

        firstPlayer=self.playerToPick

        while roundId > self.trickNb or self.checkVictory():

            roundId+=1

            firstPlayer = self.trick(firstPlayer, roundId)
    
    def gameState(self):

        for i in range(0,len(self.players[0].contractList)*len(self.players)):

            self.playerToPick.chooseContract()

            self.round()

            if self.players[-1]==self.playerToPick:

                self.playerToPick=self.players[0]

            else:

                self.playerToPick=self.players[self.players.index(self.playerToPick)+1]

        i=self.players[0].points

        win=self.players[0]

        for player in self.players:

            if player.points<i:

                i=player.points

                win=player
        
        return win
