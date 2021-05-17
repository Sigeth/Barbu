from ContractLoader import ContractLoader
import pygame, sys

class Player():

    def __init__(self, name: str):
        self.name = name
        self.deck = []
        self.points = 0
        self.rank = 0
        self.contractList = ContractLoader().loadContracts()
        self.contracts = ["Roi barbu", "Dames", "Coeurs", "Salade"] #old system : to be replaced
    
    def setName(self, screen: pygame.Surface, bgColor: tuple, font: pygame.font.Font, width: int, height: int, players: list) -> str:
        """
        Définit le nom du joueur via les inputs du clavier
        """
        current_string = []
        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:

                    if (pygame.K_0 <= event.key and event.key <= pygame.K_9) or (pygame.K_a <= event.key and event.key <= pygame.K_z):
                        current_string.append(pygame.key.name(event.key))
                    
                    elif event.key == pygame.K_BACKSPACE:
                        current_string = current_string[0:-1]
                    
                    elif event.key == pygame.K_RETURN:
                    
                        if len(current_string) == 0 or "".join(current_string) in [p.name for p in players]:
                            pass
                        else:
                            done = True
                    
                    elif event.key == pygame.K_SPACE:
                        current_string.append(" ")

            screen.fill(bgColor)
            
            chooseTxt = font.render(self.name + "'s name: " + "".join(current_string), True, (0,0,0))
            widthText, heightText = font.size(self.name + "'s name: " + "".join(current_string))
            screen.blit(chooseTxt, (width//2 - widthText//2, height//2 - heightText//2))
            pygame.display.update()
        
        self.name = "".join(current_string)
        return self.name
            

    def take(self, card):
        self.deck.append(card)

    def throw(self, card):
        self.deck.remove(card)
        return card

    def chooseCardTrick(self, deckThrow):
        print(self.name+"'s cards")
        for i in range(len(self.deck)):
            print(str(i) + " : " + self.deck[i].value.capitalize() + " de " + self.deck[i].couleur.capitalize())
        while True:
            if len(deckThrow)==0:
                choose = input("Choose the wanted card's index : ")
                try:
                    choose = int(choose)
                    return self.throw(self.deck[choose])
                except:
                    print("Invalid index provided")
            else:
                testColor=0
                colorTrick = deckThrow[0][0].couleur
                for i in range(len(self.deck)):
                    if self.deck[i].couleur==colorTrick:
                        testColor+=1
                if testColor!=0:
                    while True:
                        choose = input("Choose the wanted card's index : ")
                        try:
                            choose = int(choose)
                            assert self.deck[choose].couleur==colorTrick
                            return self.throw(self.deck[choose])
                        except:
                            print("Invalid index provided")
                else:
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
    
    def showCards(self, screen: pygame.Surface, bgColor: tuple, font: pygame.font.Font, width: int, height: int) -> pygame.Surface:
        screen.fill(bgColor)

        nameTxt = font.render(self.name + "'s turn", True, (0,0,0))
        widthText, heightText = font.size(self.name + "'s turn")

        screen.blit(nameTxt, (width//2 - widthText//2, 10))

        i = 0
        for card in self.deck:
            cardRect = card.aff.get_rect()
            cardRect.move_ip(i, height - 285)

            screen.blit(card.aff, cardRect)
            i += width//len(self.deck)

        return screen