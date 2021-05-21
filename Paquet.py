from Card import Card
from random import shuffle

class Paquet():
    """
    Paquet de cartes.
    """
    
    def __init__(self):
        """
        Construction de la liste des 52 cartes.
        """

        couleur = ('pique', 'trèfle', 'carreau', 'coeur')
        valeur = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi')
        self.cartes = []

        for coul in range(4):

            for val in range(13):

                nouvelle_carte = Card(valeur[val], couleur[coul],val)   # la valeur commence à  0
                self.cartes.append(nouvelle_carte)

        self.battre()


    def battre(self):
        """
        Mélanger les cartes.
        """

        shuffle(self.cartes)
        

    def tirer(self) -> Card:
        """
        Tirer la première carte de la pile.
        """

        t = len(self.cartes)

        if t>0:

            carte = self.cartes[0]   # choisir la première carte du jeu
            del(self.cartes[0])      # et la supprimer du jeu
            return carte

        else:
        
            return None
    

    def remettre(self, card: Card):
        """
        Remettre la carte dans le paquet.
        """

        self.cartes.append(card)
