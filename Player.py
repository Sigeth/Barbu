from ContractLoader import ContractLoader
import pygame, sys
from Card import Card

class Player():

    def __init__(self, name: str):
        self.name = name
        self.deck = []
        self.points = 0
        self.rank = 0
        self.contractList = ContractLoader().loadContracts()
    
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
            

    def take(self, card: Card):
        """
        
        """
        self.deck.append(card)

    def throw(self, card: Card) -> Card:
        self.deck.remove(card)
        return card

    def chooseCardTrick(self, deckThrow: tuple, i: int) -> Card:
        if len(deckThrow)==0:
            return self.throw(self.deck[i])
        else:
            testColor=0
            colorTrick = deckThrow[0][0].couleur
            for j in range(len(self.deck)):
                if self.deck[j].couleur==colorTrick:
                    testColor+=1
            if testColor!=0:
                while True:
                    try:
                        assert self.deck[i].couleur==colorTrick
                        return self.throw(self.deck[i])
                    except:
                        pass
            else:
                return self.throw(self.deck[i])
                    
    
    def addPoints(self, points: int):
        self.points += points
    
    def removePoints(self, points: int):
        self.points -= points
    
    def chooseContract(self, i: int) -> dict:
        return self.contractList.pop(i)
            
        
    def waitingScreen(self, screen: pygame.Surface, bgColor: tuple, font: pygame.font.Font, width: int, height: int) -> pygame.Surface:
        screen.fill(bgColor)

        waitingTxt = font.render(self.name + ", press Enter to play", True, (0,0,0))
        widthTxt, heightTxt = font.size(self.name + ", press Enter to play")

        screen.blit(waitingTxt, (width//2 - widthTxt//2, height//2 - heightTxt//2))

        return screen

        
    
    def showCards(self, screen: pygame.Surface, bgColor: tuple, font: pygame.font.Font, width: int, height: int) -> tuple:
        screen.fill(bgColor)

        nameTxt = font.render(self.name + "'s turn", True, (0,0,0))
        widthText, heightText = font.size(self.name + "'s turn")

        screen.blit(nameTxt, (width//2 - widthText//2, 10))

        cardRects = []

        i = 0
        for card in self.deck:
            cardRect = card.aff.get_rect()
            cardRect.move_ip(i, height - 285)

            cardRects.append(cardRect)

            screen.blit(card.aff, cardRect)
            i += width//len(self.deck)

        return screen, cardRects
    
    def showContracts(self, screen: pygame.Surface, bgColor: tuple, font: pygame.font.Font, width: int, height: int) -> tuple:

        cardRects = []

        for i in range(len(self.contractList)):
            el = self.contractList[i]

            card = Card(el["cardToDisplay"]["value"], el["cardToDisplay"]["couleur"], el["cardToDisplay"]["n"])



            cardRect = card.aff.get_rect()
            cardRect.move_ip(i*(width//len(self.contractList)) + 192//3, height//2 - 280//2)

            cardRects.append(cardRect)

            screen.blit(card.aff, cardRect)
        
        return screen, cardRects

