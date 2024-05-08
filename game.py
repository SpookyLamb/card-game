# Must Have (DONE)
    # 1. Use OOP - have at least a deck class, a card class, and a player class (DONE)
    # 2. Use PyTest - write at least two tests (DONE)
    # 3. Shuffle the deck (DONE)
    # 4. Player selects how many decks to use (DONE)
    # 5. Deal the player and the dealer (computer) 1 card each (DONE)
    # 6. High card wins - suit breaks ties (DONE)
    # 7. Track number of wins (DONE)

# Should Have (DONE)
    # 1. Input Player name (DONE)
    # 2. Handle betting: (DONE)
    # ● The player places a bet before they get their cards. (DONE)
    # ● If player loses then they lose their bet amount (DONE)
    # ● If player wins then they get double their bet amount (DONE)
    # ● Track how much the player has won/lost (DONE)

# Could Have
    # 1. Multiple Players
    # 2. BlackJack
    # ● Player and dealer get 2 cards to start - player can only see one of the dealer cards
    # ● If dealer has less than 17 they have to take a card, over 17 they stop (dealer is automated)
    # ● Player goes first and can take as many cards as they want until they stop or they are over 21 (bust)
    # 3. User selects game at start (BlackJack or High Card)

# Wish List
    # 1. War
    # ● Player and computer each get half the cards
    # ● Each player turns over one card - high card wins (suit doesn’t matter)
    # ● In case of tie, place 3 cards each and then high card wins
    # ● Game plays until one player has all the cards
    # ● Have the game auto play from start to finish, show all moves.

import random
import math

player_name = "Sin Nombre"

#classes

class Card():
    def __init__(self, value, suit) -> None:
        # Cards have two values, their numbered value and their suit

        # 1 is Ace
        # 2-10 correspond to numbered cards
        # 11 is Jack, 12 is Queen, 13 is King
        # Suits (in order of priority, high to low) are Spades, Hearts, Diamonds, and Clubs, represented by strings

        self.value = value
        self.suit = suit
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value

class Deck():
    def shuffle(self, refresh = False):
        #shuffles the deck, refresh is a bool, false by default
        #if refresh is true, adds discard to deck, empties it, and then shuffles the cards
        #otherwise, just shuffle what's already there

        if refresh:
            self.deck = self.deck + self.discard

        random.shuffle(self.deck)
        #print("Deck shuffled.")

    def empty(self): #checks if a deck is empty
        if len(self.deck) > 0:
            return False
        else:
            return True

    def draw(self):
        #pops (removes) and returns the last element in the deck
        return self.deck.pop()
    
    def discarded(self, card):
        #takes a discarded card and adds it to the discard
        self.discard.append(card)
    
    def __init__(self) -> None:
        #sets a basic 52 card deck by filling an array with card classes  

        self.deck = [] 
        self.discard = [] #empty on ready, filled when a card is used

        #fill our cards with a nested loop
        for i in range(13):
            #add each of the basic 13 cards...
            for j in range(4):
                #...in each suit
                suit = ""

                match j:
                    case 0:
                        suit = "Spade"
                    case 1:
                        suit = "Heart"
                    case 2:
                        suit = "Diamond"
                    case _: #3, default
                        suit = "Club"

                card = Card(i + 1, suit) #counts from zero, add 1 to i for the value
                self.deck.append(card)
                #print(card.get_value(), " ", card.get_suit())
        
        #once we're done, shuffle the deck
        self.shuffle(self.deck)

class Player():
    def __init__(self, deck) -> None:
        self.deck = deck
        self.bank = 1000 #$1000 to start!
    
    def get_deck(self):
        return self.deck
    
    def draw(self):
        if self.deck.empty():
            self.deck.shuffle(True)

        return self.deck.draw()
    
    def discard(self, card):
        self.deck.discarded(card)

#tests

def test_names():
    assert (name_cards(11) == "Jack")

def test_compare():
    card = Card(8, "Spade")
    assert (compare_cards(card, card) == "TIE")

#functions

def br():
    print("")

def check_num(inputty):
    val = 0

    try:
        val = int(inputty)
        return val
    except:
        return val #return 0 as a failure

def compare_cards(card1, card2):
    #takes two cards, returns the winning card or "TIE" if it's a tie
    
    value1 = card1.value
    value2 = card2.value

    if value1 > value2:
        return card1
    elif value2 > value1:
        return card2
    else: #tie
        #compare suits, S > H > D > C
        comp = {
            "Spade": 4,
            "Heart": 3,
            "Diamond": 2,
            "Club": 1
        }

        suit1 = card1.suit
        suit2 = card2.suit

        if comp[suit1] > comp[suit2]:
            return card1
        elif comp[suit2] > comp[suit1]:
            return card2
        else: #total tie
            return "TIE"

def invalid():
    print("Invalid input! Try again.")

def name_input():
    global player_name
    new_name = input("Hello! What's your name? ")

    if new_name: #keep "sin nombre" if the name field is empty
        player_name = new_name

def yes_or_no(inpy):
    #checks if an input is valid as yes or no
    inpy = inpy.upper()

    if inpy == "Y" or inpy == "YES":
        return True
    elif inpy == "N" or inpy == "NO":
        return False
    else:
        invalid()
        return "inv"

def play_again():
    #returns true (play again) or false (don't)
    valid_input = False

    while not valid_input:
        player_input = input("Play again (Yes/No)? ")
        result = yes_or_no(player_input)

        if result == "inv":
            continue #skip, try again
        else:
            valid_input = True
            return result
    
    return False #fail safe, this should never fire

def name_cards(card_value):
    names = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
    } #others are printed as is

    if card_value in names:
        return names[card_value]
    else:
        return card_value

def name_format(card_value, card_suit):
    #returns a string with a card's name formatted as "VALUE of SUIT"
    return str(card_value) + " of " + str(card_suit) + "s"

def select_game():
    #asks the player to select a game
    pass

def high_card():
    #HIGH CARD - player and dealer both draw a card and compare them, either from the same deck or two distinct decks
    
    #init
    valid_input = False
    player = None
    dealer = None

    br()
    print("HIGH CARD - LOW CARD")
    br()

    while not valid_input:
        player_input = check_num(input("How many decks do you want to use (1 or 2)? "))

        if player_input == 1:
            valid_input = True
            print("Then you'll share with me...")

            deck = Deck()
            player = Player(deck)
            dealer = Player(deck)
        
        elif player_input == 2:
            valid_input = True
            print("Then we'll use different decks.")

            player = Player(Deck())
            dealer = Player(Deck())

        else: #throw, try again
            invalid()

    playing = True
    round_count = 0
    player_wins = 0
    dealer_wins = 0
    total_winnings = 0
    
    while playing:
        #this loop covers the actual game
        round_count += 1

        #start round
        br()
        print("ROUND ", round_count)

        #take bets
        valid_input = False

        while not valid_input:
            bet = check_num(input(f"How much are you betting? (${player.bank} Available) "))

            if bet > player.bank:
                print("You don't have that kind of money! Try again.")
            elif bet < 0:
                print("You can't bet NEGATIVE money! Try again.")
            else:
                print(f"Betting ${bet}...")
                valid_input = True

        #DRAW
        br()

        player_card = player.draw()
        val1 = name_cards(player_card.value)
        
        dealer_card = dealer.draw()
        val2 = name_cards(dealer_card.value)

        #give the player the chance to look at their card and fold to lose only half their bet, if they want
        valid_input = False
        folded = False
        
        while not valid_input:
            player_input = input("Your card is: " + name_format(val1, player_card.suit) + ". Fold (Y/N)? ")
            result = yes_or_no(player_input)

            if result == "inv":
                continue #try again
            elif result: #folded
                valid_input = True
                folded = True

                loss = math.floor(bet / 2) #rounded down, because we're nice
                player.bank -= loss
                total_winnings -= loss

                print("You folded (and lost HALF your bet)...") 
            else: #proceed
                valid_input = True
                break

        if not folded:
            #input("Press enter when you're ready to reveal the dealer's card...")
            br()
            #print(f"{player_name}'s card: " + name_format(val1, player_card.suit))
            print("Dealer's card: " + name_format(val2, dealer_card.suit))

            winner = compare_cards(player_card, dealer_card)

            br()

            if winner == player_card: #player win
                print(f"{player_name} wins!")
                player_wins += 1
                player.bank += 2 * bet
                total_winnings += 2 * bet
            elif winner == dealer_card: #dealer win
                print("Dealer wins!")
                dealer_wins += 1
                player.bank -= bet
                total_winnings -= bet
            else: #tie
                print("Tie!") #mulligan, don't do anything else
        
        #discard cards
        player.discard(player_card)
        dealer.discard(dealer_card)

        #track wins
        br()
        print(f"{player_name} win count: ", player_wins)
        print("Dealer win count: ", dealer_wins)
        br()
        print("Total winnings: ", "$" + str(total_winnings))
        print("Bank: ", "$" + str(player.bank))

        #at the end of our loop, ask the player if they want to play again
        br()
        playing = play_again()

name_input()

high_card()