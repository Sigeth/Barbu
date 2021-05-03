from Player import Player
from Paquet import Paquet
from random import choice

class Game():

    def __init__(self, nbPlayers=4, nbCards=52):
        self.paquet = Paquet()
        self.players = [Player() for i in range(nbPlayers)]
        for i in range(nbCards//nbPlayers):
            for p in self.players:
                p.take(self.paquet.tirer())
        self.playerToPick = choice(self.players)
        self.roundNb = len(self.players[0].deck)





game = Game()
for p in game.players:
    print("Cartes d'un nouveau joueur uwu")
    for c in p.deck:
        print(str(c.value) + " de " + c.couleur)
    print(p.points)
        

    
    



