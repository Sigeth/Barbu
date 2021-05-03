from Player import Player
from Paquet import Paquet
from random import choice

class Game():

    def __init__(self, nbPlayers=4, nbCards=52):
        self.nbPlayers = nbPlayers
        self.nbCards = nbCards
        self.paquet = Paquet()
        self.players = [Player() for i in range(nbPlayers)]
        self.draw()
        self.playerToPick = choice(self.players)
        self.roundNb = len(self.players[0].deck)
    
    def draw(self):
        self.clearDecks()
        for i in range(self.nbCards//self.nbPlayers):
            for p in self.players:
                p.take(self.paquet.tirer())
            
    def clearDecks(self):
        for p in self.players:
            p.deck = []

    def trick(self):
        




game = Game()
for p in game.players:
    print("Cartes d'un nouveau joueur uwu")
    for c in p.deck:
        print(str(c.value) + " de " + c.couleur)
    print(p.points)
        
for i in range(len(game.playerToPick.contracts)):
    choice = game.playerToPick.pick()
    currentContract = Contract(choice)
    while currentContract.isPlayable:
