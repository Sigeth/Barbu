from Player import Player
from Paquet import Paquet
from random import choice

class Game():

    def __init__(self, nbPlayers=4, nbCards=52):
        self.nbPlayers = nbPlayers
        self.nbCards = nbCards
        self.paquet = Paquet()
        self.players = [Player("Player " + str(i+1)) for i in range(nbPlayers)]
        self.currentContract = None
        self.draw()
        self.playerToPick = choice(self.players)
        self.trickNb = len(self.players[0].deck)
        self.roundNb = len(self.players[0].contracts)
    
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
        #return winner
        pass


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
            for  el in deckThrow:
                card = el[0]
                if (card.value == "roi" and card.couleur == "coeur") and (self.currentContract == "Roi Barbu" or self.currentContract == "Salade"):
                    winner[1].addPoints(100)
                elif (card.value == "dame") and (self.currentContract == "Dames" or self.currentContract == "Salade"):
                    winner[1].addPoints(25)
                if (card.couleur == "coeur") and (self.currentContract == "Coeurs" or self.currentContract == "Salade"):
                    #TO-DO
                    pass
        pass
        
    def checkVictory(self):
        #todo boolean function to check if anyone has won
        pass
    
    def round(self):
        roundId = 0
        firstPlayer=self.playerToPick 
        while roundId > self.trickNb or self.checkVictory():
            roundId+=1
            firstPlayer = self.trick(firstPlayer)
            
    