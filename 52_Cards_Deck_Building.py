import random

class Card:
    def __init__(self, cardNumber, cardSuit):
        self.cardNumber = cardNumber
        self.cardSuit = cardSuit



#Testing for GitHub
    
#I want to build BlackJack, where the dealer deals a card to the player
#The player bets an amount of money before they see their cards
#Then the dealer deals a card to themselves, this happens until they have 2 cards
#I want to have a print statement that tells the player their hand
#I want to have a print statement that tells the player the dealers hand
#The goal of BlackJack is to see who can get or be closest to 21 without going over
#The player starts and decides if they want to hit (draw a card off the top of the deck and add it to their hand)
#If the player decides to keep going until they want to stop. 
#Then the dealer does the same. 
#If the player beats the dealer, they win the bet. 
#If they lose, they lose their bet. 
#The player plays until they've decided they no longer want to play or they've lost all of their money

class Person:
    
    def __init__(self):
        self.cardsInHand = []
        self.handValue = 0
        self.currentMoney = 1000
        self.name = ""

    def AddCardToHand(self, card):
        self.cardsInHand.append(card)

class Deck:
    cardsList = []
    deck = {}
    
    def __init__(self):
        self.AddCardsToDeck()
        

    def MakeCard(self, suit):
        cards = []
        count = 1
        while count < 14:
            self.card = Card(count, suit)
            if(count == 1):
                self.card.cardNumber = "Ace"
            if(count == 11):
                self.card.cardNumber = "Jack"
            if(count == 12):
                self.card.cardNumber = "Queen"
            if(count == 13):
                self.card.cardNumber = "King"
            cards.append(self.card)
            count += 1
        return cards
    
    def AddCardsToDeck(self):
        self.deck["Spades"] = self.MakeCard("Spades")
        self.deck["Hearts"] = self.MakeCard("Hearts")
        self.deck["Clubs"] = self.MakeCard("Clubs")
        self.deck["Diamonds"] = self.MakeCard("Diamonds")
        #Loops through the dictionary for each suit
        for suit, l in self.deck.items():
            #Loops through each list for a card
            for card in l:
                #Adds the card to the deck
                self.cardsList.append(card)
        
    def DealACard(self, person):
        person.cardsInHand.append(self.cardsList[0])
        print(f"The card dealt to {person.name} is the {self.cardsList[0].cardNumber} of {self.cardsList[0].cardSuit}.")
        person.handValue += CardValue(self.cardsList[0])
        self.cardsList.pop(0)

    def ShuffleDeck(self):
        random.shuffle(self.cardsList)
        print("The dealer shuffles the deck.")

def main(args):
    dealer = Person()
    player = Person()
    dealer.name = "Dealer"
    player.name = input("Hey, what's your name? ")
    wantsToPlay = True
    theDeck = Deck()
    theDeck.ShuffleDeck()
    PlayerTurn(player, theDeck)
    '''
    while wantsToPlay == True and player.currentMoney > 0:
        GamePlayLoop(theDeck, player, dealer)
    '''    
    

    
def StartBlackJack(deck, player, dealer):
    deck.ShuffleDeck()
    #PlaceBet()
    for i in range(2):
        deck.DealACard(player)
        deck.DealACard(dealer)

def PlaceBet(player):
    validBet = False
    print(f"You currently have ${player.currentMoney}. How much would you like to bet?")
    while validBet == False:
        playerCurrentBet = input()
        try:
            playerCurrentBet = int(playerCurrentBet)
            if(playerCurrentBet <= player.currentMoney and playerCurrentBet > 0):
                print(f"You have bet ${playerCurrentBet}")
                validBet = True
            else:
                print("That is not a valid amount.")
        except:
            print("That is not a valid input.")


def LostRound(person):
    print(f"You've lost this round.\nYour current amount of money is ${person.currentMoney}.")
    validInput = False
    playAgain = False
    
    while validInput == False:
        userInput = input("Would you like to play again?\nYes or No?\n")
        try:
            if userInput.upper() == "YES":
                validInput = True
                playAgain = True
            if userInput.upper() == "NO":
                validInput = True
                playAgain = False
        except:
            print("That is not valid input.")
    return playAgain

def GamePlayLoop(deck, player, dealer):
    PlaceBet(player)
    StartBlackJack(deck, player, dealer)
    PlayerTurn(player, deck)

def HandStatus(person):
    print(f"{person.name} currently has {len(person.cardsInHand)} card(s) in hand.")
    for i in range(len(person.cardsInHand)):
        print(f"The {person.cardsInHand[i].cardNumber} of {person.cardsInHand[i].cardSuit}")
        
    print(f"The card(s) in your hand total to {person.handValue}.")

def PlayerTurn(player, deck):
    HandStatus(player)
    wantToStay = False
    while wantToStay == False:
        userInput = input("Would you like to hit or stay? ")
        try:
            if userInput.upper() == "HIT":
                deck.DealACard(player)
                HandStatus(player)
            elif userInput.upper() == "STAY":
                wantToStay = True
            else:
                "That is not valid input."
        except:
            "That is not valid input."


def CardValue(card):
    cardValue = 0
    value = False
    if card.cardNumber == "Ace":
        while value == False:
            userInput = input("Would you like this Ace to be counted as 1 or 11? ")
            try:
                if int(userInput) == 1 or int(userInput) == 11:
                    cardValue = int(userInput)
                    value = True
                else:
                    print("That is not a valid number.")
            except:
                print("That is not a valid input.")
    elif card.cardNumber == "Jack" or card.cardNumber == "Queen" or card.cardNumber == "King":
        cardValue = 10
    else:
        cardValue = card.cardNumber

    return cardValue



if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))

