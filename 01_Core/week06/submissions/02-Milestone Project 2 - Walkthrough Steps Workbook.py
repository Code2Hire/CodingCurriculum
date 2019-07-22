

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: '+ deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        new_card = card
        self.cards.append(new_card)
        self.value += values[new_card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input('Enter your bet: '))
        
        except:
            print('Invalid bet, must be an integer')
        else:
            if chips.bet > chips.total:
                print('Not enough chips')
            else:
                break # Necessary to exit the while loop
                

def hit(deck,hand):
    a_deck = deck
    a_hand = hand
    a_hand.add_card(a_deck.deal())
    a_hand.adjust_for_ace
    

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    a_deck = deck
    a_hand = hand
    while True:
        choice = input("Hit or Stand? (H/S)")
        if choice.upper() == 'H':
            hit(a_deck,a_hand)
        elif choice.upper() == 'S':
            print("--Dealer's Turn--")
            playing = False
        else:
            print('Invalid input, please enter "H" or "S"')
            continue
        break

def show_some(player,dealer):
    print("Dealer's hand:")
    print('-Facedown card-')
    print(dealer.cards[1])
    print('\n')
    print('Your hand:')
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    print("Dealer's hand:")
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Your hand:')
    for card in player.cards:
        print(card)


def player_busts(player, dealer, chips):
    print('Your hand value is over 21-> You lose')
    chips.lose_bet()
def player_wins(player, dealer, chips):
    print("Your hand beat the dealer's ->You win!")
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print('The dealer busted -> You win!')
    chips.win_bet()
def dealer_wins(player, dealer, chips):
    print("The dealer's hand was stronger -> You lose")
    chips.lose_bet()
def push(player, dealer):
    print('You and the dealer tied -> Push')

while True:
    # Print an opening statement
    print('BLACKJACK')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    p_hand = Hand()
    p_hand.add_card(deck.deal())
    p_hand.add_card(deck.deal())
    
    d_hand = Hand()
    d_hand.add_card(deck.deal())
    d_hand.add_card(deck.deal())
    
    
    # Set up the Player's chips
    p_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(p_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(p_hand, d_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, p_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(p_hand, d_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if p_hand.value > 21:
            player_busts(p_hand, d_hand, p_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if p_hand.value <= 21:
        while d_hand.value < p_hand.value:
            hit(deck, d_hand)
        # Show all cards
        show_all(p_hand, d_hand)
        # Run different winning scenarios
        if d_hand.value > 21:
            dealer_busts(p_hand, d_hand, p_chips)
        elif d_hand.value > p_hand.value:
            dealer_wins(p_hand, d_hand, p_chips)
        elif d_hand.value < p_hand.value:
            player_wins(p_hand, d_hand, p_chips)
        else:
              push(p_hand, d_hand)
        
              
    
    # Inform Player of their chips total 
    print(f'Your chip count: {p_chips.total}')
    # Ask to play again
    choice  = input ("Play again? (Y/N)")
    if choice.upper() == "Y":
        playing = True
        continue
    else:
        print('Exiting game...')
    break
