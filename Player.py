class Player():
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.points = 0
        self.rank = 0
        self.contracts = ["Roi barbu", "Dames", "Coeurs", "Pli", "Dernier pli", "Salade"]
    
    def setName(self):
        self.name = input(self.name + ", choisissez un nom")

    def take(self, card):
        self.deck.append(card)

    def throw(self, card):
        self.deck.remove(card)
        return card

    def chooseCardTrick(self):
        print(self.name+"'s cards")
        for i in range(len(self.deck)):
            print(str(i) + " : " + self.deck[i].value.capitalize() + " de " + self.deck[i].couleur.capitalize())
        while True:
            choose = input("Choose the wanted card's index : ")
            try:
                choose = int(choose)
                return self.throw(self.deck[choose])
            except:
                print("Invalid index provided")

    
    def addPoints(self, points):
        self.points += points
    
    def removePoints(self, points):
        self.points -= points
    
    def chooseContract(self):
        print(self.name+"'s contracts")
        for i in range(len(self.contracts)):
            print(str(i) + " : " + self.contracts[i])
        while True:
            choose = input("Choose the wanted contract's index : ")
            try:
                choose = int(choose)
                return self.contracts.pop(choose)
            except:
                print("Invalid index provided")