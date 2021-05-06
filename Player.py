from ContractLoader import ContractLoader
import pygame

class Player():

    def __init__(self, name):
        self.name = name
        self.deck = []
        self.points = 0
        self.rank = 0
        self.contractList = ContractLoader().loadContracts()
        print(self.contractList) #debug
        self.contracts = ["Roi barbu", "Dames", "Coeurs", "Pli", "Dernier pli", "Salade"] #old system : to be replaced
    
    def setName(self, screen, font, width, height):
        current_string = []
        chooseTxt = font.render(self.name + "'s name: " + "".join(current_string), True, (0,0,0))
        widthText, heightText = font.size(self.name + "'s name: " + "".join(current_string))
        screen.blit(chooseTxt, (width//2 - widthText//2, height//2 - heightText//2))
        while True:
            screen.fill((255, 255, 255))
            #print(pygame.key.get_pressed())
            """if inkey == K_BACKSPACE:
                current_string = current_string[0:-1]
            elif inkey == K_RETURN:
                break
            elif inkey == K_MINUS:
                current_string.append("_")
            elif inkey <= 127:
                current_string.append(chr(inkey))"""
            chooseTxt = font.render(self.name + "'s name: " + "".join(current_string), True, (0,0,0))
            widthText, heightText = font.size(self.name + "'s name: " + "".join(current_string))
            screen.blit(chooseTxt, (width//2 - widthText//2, height//2 - heightText//2))
            pygame.display.update()
        self.name = string.join(current_string,"")
        return self.name

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