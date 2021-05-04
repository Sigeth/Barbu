#from Game import Game
from Player import Player
from Paquet import Paquet

p = Player("Player 1")

contract = p.chooseContract()
print(contract)

"""game = Game()
for p in game.players:
    print("Cartes d'un nouveau joueur uwu")
    for c in p.deck:
        print(str(c.value) + " de " + c.couleur)
    print(p.points)
        
for i in range(len(game.playerToPick.contracts)):
    choice = game.playerToPick.pick()
    currentContract = Contract(choice)
    while currentContract.isPlayable:
        #todo"""
