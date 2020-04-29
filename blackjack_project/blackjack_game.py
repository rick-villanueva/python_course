'''
1. Create a deck of 52 cards 
2. Shuffle the deck 
3. Ask the Player for their bet 
4. Make sure that the Player's bet does not exceed their available chips 
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden 
7. Show both of the Player's cards 
8. Ask the Player if they wish to Hit, and take another card 
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again. 
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17 
11. Determine the winner and adjust the Player's chips accordingly 12. Ask the Player if they'd like to play again
'''

#Global parameters
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#Create a Card class
class Card:
    
    def __init__(self,suit,rank:
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '{} of {}'.format(self.rank,self.suit)
    
#Create a deck class
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                                
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'Deck:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Hand class    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
#Chips class
class Chips:
    
    def __init__(self,total=100):
        self.total = total # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self,self.bet):
        self.total += self.bet
        
    
    def lose_bet(self,self.bet):
        self.total -= self.bet

#Take bets
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break
                
#Hits
def hit(deck,hand):
    
    hand.add_card(deck.deal()) #call methods defined in previous classes
    hand.adjust_for_ace()
        
        
#Hit or stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
 
#Show partial hands      
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

#Show all hands
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
#Check wins
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("House busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("House wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("House and Player tie! It's a push.")