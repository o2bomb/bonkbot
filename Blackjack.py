import random

class Card:
    def __init__(self, suit, val, pic):
        self.suit = suit
        self.value = val
        self.picture = pic

    def show(self):
        print("{} of {}".format(self.picture, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            self.cards.append(Card(s, 1, "Ace"))
            for v in range(2, 11):
                self.cards.append(Card(s, v, v))
            for p in ["Jack", "Queen", "King"]:
                self.cards.append(Card(s, 10, p))

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
    
    def show(self):
        for c in self.cards:
            c.show()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.funds = 100
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()

class PlayerList:
    def __init__(self):
        self.playerdict = {}

    def add(self, player):
        self.playerdict[player.name] = player

    
def gameRound(pName):
    f = input("Hit (H), Stand (S), Double (D) or  Split (Sp)?\n")
    f.replace(" ", "")
    if f != "H" and f != "S" and f != "D" and f != "Sp":
        print("Invalid command.")
    else:
        if f == "H":
            pl.playerdict[pName].draw(deck)
            pl.playerdict[pName].showHand()
        elif f == "S":
            pass
        elif f == "D":
            pass
        elif f == "Sp":
            pass
    
def main():
    dealer = Player("d")
    f = input("Your name?\n")
    player = Player(f)
    player.draw(deck)
    player.draw(deck)
    pl.add(player)
    dealer.draw(deck)
    print(f + " has")
    player.showHand()
    print("\nDealer has")
    dealer.showHand()
    gameRound(player.name)
    
    
pl = PlayerList()
deck = Deck()
deck.shuffle()
main()
