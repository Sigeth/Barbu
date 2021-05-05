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

        self.currentState = "WaitingRoom"

        self.size = self.width, self.height = 1280, 720

        self.bgColor = 255, 255, 255

        pygame.display.set_caption("Jeu du Barbu")
        icon = pygame.image.load("src/icon.png")
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode(self.size)

<<<<<<< Updated upstream
=======
        self.fontSrc = "src/KGRedHands.ttf"
        self.fontSize = 96

>>>>>>> Stashed changes
        self.waitingRoom()
    

    def waitingRoom(self):
        launchButtonColor = 138, 43, 226

        self.paquet.battre()

<<<<<<< Updated upstream
        font = pygame.font.Font("src/KGRedHands.ttf", 96)
        widthText, heightText = font.size("LAUNCH")



        while currentState == "WaitingRoom":
=======
        font = pygame.font.Font(self.fontSrc, self.fontSize)
        widthText, heightText = font.size("LAUNCH")

        delayms = 1000
        currentDelay = 1000
        cardsToDisplay = [None for i in range(6)]
        while self.currentState == "WaitingRoom":
>>>>>>> Stashed changes
            mouseX, mouseY = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
<<<<<<< Updated upstream
            screen.fill(bgColor)

            if currentDelay >= delayms:
                for i in range(6):
                    card = choice(paquet.cartes)
=======
            self.screen.fill(self.bgColor)

            if currentDelay >= delayms:
                for i in range(6):
                    card = choice(self.paquet.cartes)
>>>>>>> Stashed changes
                    cardRect = card.aff.get_rect()
                    widthCard, heightCard = (0, 0)
                    if i == 0 or i == 3:
                        widthCard = 50
                    elif i == 1 or i == 4:
<<<<<<< Updated upstream
                        widthCard = width//2 - 192//2
                    else:
                        widthCard = width - 50 - 192
=======
                        widthCard = self.width//2 - 192//2
                    else:
                        widthCard = self.width - 50 - 192
>>>>>>> Stashed changes
                    
                    if i < 3:
                        heightCard = 0
                    else:
<<<<<<< Updated upstream
                        heightCard = height - 290
=======
                        heightCard = self.height - 290
>>>>>>> Stashed changes
                    
                    cardRect.move_ip(widthCard, heightCard)
                    cardsToDisplay[i] = (card.aff, cardRect)
                currentDelay = 0

            for card, cardRect in cardsToDisplay:
<<<<<<< Updated upstream
                screen.blit(card, cardRect)

            colorText = (0, 0, 0)
            if (width//2 - widthText//2 < mouseX and mouseX < width//2 + widthText//2) and (height//2 - heightText//2 < mouseY and mouseY < height//2 + heightText//2):
                colorText = (randint(0, 255), randint(0, 255), randint(0, 255))
                if pygame.mouse.get_pressed(3)[0]:
                    game = Game()
                    game.launch()

            launchTxt = font.render("LAUNCH", True, colorText)
            screen.blit(launchTxt, (width//2 - widthText//2, height//2 - heightText//2))
=======
                self.screen.blit(card, cardRect)

            colorText = (0, 0, 0)
            if (self.width//2 - widthText//2 < mouseX and mouseX < self.width//2 + widthText//2) and (self.height//2 - heightText//2 < mouseY and mouseY < self.height//2 + heightText//2):
                colorText = (randint(0, 255), randint(0, 255), randint(0, 255))
                if pygame.mouse.get_pressed(3)[0]:
                    self.launch()

            launchTxt = font.render("LAUNCH", True, colorText)
            self.screen.blit(launchTxt, (self.width//2 - widthText//2, self.height//2 - heightText//2))
>>>>>>> Stashed changes
            pygame.display.update()
            currentDelay += 1


    def draw(self):

        self.clearDecks()

        self.paquet.battre()

        for i in range(self.nbCards//self.nbPlayers):

            for p in self.players:

                p.take(self.paquet.tirer())
            

    def clearDecks(self):

        for p in self.players:

            p.deck = []
        

    def launch(self):

        for p in self.players:

            p.setName()

        self.changeContract(self.playerToPick)
        self.round()


    def changeContract(self, p):

        self.currentContract = p.chooseContract()


    def trick(self, firstPlayer,roundId):

        deckThrow = []

        index = self.players.index(firstPlayer)

        for i in range(len(self.players)):

            player = self.players[index + i - (4*((index+i)//4))]

            card = player.chooseCardTrick()

            deckThrow.append((card,player))

        self.calculatePoints(deckThrow,roundId)

        return winner



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

        firstPlayer=self.playerToPick
        while roundId > self.trickNb or self.checkVictory():

            roundId+=1

            firstPlayer = self.trick(firstPlayer, roundId)
