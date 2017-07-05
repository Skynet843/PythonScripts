# WARNING : Game may get into an infinite loop.
from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:

    def __init__(self):
        self.deck = [i + j for i in SUITE for j in RANKS]

        shuffle(self.deck)

    def cardp1(self):
        return self.deck[0:26]

    def cardp2(self):
        return self.deck[26:52]


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def show(self):
        print(self.cards)

    def remove(self, card):
        self.cards.remove(card)

    def add(self, card):
        for i in card:
            self.cards.append(i)


class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return self.name

    def playcard(self):
        c = self.hand.cards[0]
        self.hand.cards.remove(c)
        return c

    def isempty(self):
        if len(self.hand.cards) == 0:
            return True
        else:
            return False


def showCard(c):

    try:
        c1 = int(c[1])
        return c1

    except:
        if c[1] == 'J':
            return 11

        elif c[1] == 'Q':
            return 12

        elif c[1] == 'K':
            return 13

        elif c[1] == 'A':
            return 14


print("Welcome to War, let's begin...")

deck = Deck()

h1 = Hand(deck.cardp1())
h2 = Hand(deck.cardp2())

p1name = input("Enter your name : ")

p1 = Player(p1name, h1)
p2 = Player('Computer', h2)


def over():
    if p1.isempty() or p2.isempty():
        return True
    else:
        return False

rounds = 0
wars = 0
while(1):

    if(over()):
        break

    rounds += 1
    c1 = p1.playcard()
    c2 = p2.playcard()

    pc1 = showCard(c1)
    pc2 = showCard(c2)

    if(pc1 > pc2):
        p1.hand.add([c1, c2])

    elif pc1 < pc2:
        p2.hand.add([c1, c2])

    elif pc1 == pc2:
        four_p1 = []
        four_p2 = []
        wars += 1
        for i in range(4):
            if(over()):
                break
            four_p1.append(p1.playcard())
            four_p2.append(p2.playcard())

        if(over()):
            break

        if(four_p2[-1] < four_p1[-1]):
            p1.hand.add(four_p2)
            p1.hand.add(four_p1)

        else:
            p2.hand.add(four_p2)
            p2.hand.add(four_p1)


if(p1.isempty()):
    print("\nComputer won")
else:
    print(p1,end='')
    print(" won")

print("Rounds : {}\nWars : {}".format(rounds, wars))
