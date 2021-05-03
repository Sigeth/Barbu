from Contract import Contract

class Player():
    def __init__(self):
        self.deck = []
        self.points = 0
        self.rank = 0
        #self.contracts = [Contract("Pli")]
    
    def take(self, card):
        self.deck.append(card)

    def withdraw(self, card):
        self.deck.pop(card)
    
    def addPoints(self, points):
        self.points += points
    
    def removePoints(self, points):
        self.points += points
    