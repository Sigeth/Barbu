class Player():
    def __init__(self):
        self.deck = []
        self.points = 0
        self.rank = 0
        self.contracts = ["Roi de coeur", "Dames", "Coeurs", "Pli", "Dernier pli", "Salade"]
    
    def take(self, card):
        self.deck.append(card)

    def throw(self, card):
        self.deck.pop(card)
    
    def addPoints(self, points):
        self.points += points
    
    def removePoints(self, points):
        self.points -= points
    
    def pick(self, name):
        print("Vous avez le choix entre plusieurs contrats :")
        print("\n".join(self.contracts))