import random
from IPython.display import clear_output
from pandas import DataFrame
          
class Card():
    
    def __init__(self, card_name):
        self.name = card_name
        values = {"Ace":11,"Two":2,"Three":3, "Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,'King':10}
        self.value = values[card_name.split()[0]]
        
    def __str__(self):
        return self.name
    
    def __add__(self,card):
        list_cards = [self.name]
        list_cards.append(card.name)
        return list_cards
    
class Deck():
    
    def __init__(self):
        self.card_set=[]
        suits = ["Spades","Hearts","Clubs","Diamonds"]
        card_num = ["Ace", "Two",'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
        
        for suit in suits:
            for num in card_num:
                self.card_set.append(f"{num} of {suit}")
        
        self.length = len(self.card_set)
    
    def shuffle(self):
        random.shuffle(self.card_set)

    def deal(self):
        self.length-=2
        return [Card(self.card_set.pop()),Card(self.card_set.pop())]
    
    def hit(self):
        self.length-=1
        return Card(self.card_set.pop())

    
    def __str__(self):
        return str(self.card_set)

class Hand():
    
    def __init__(self, cards):
        self.cards = cards
        
        #Sum of the hand
        self.sum = 0
        for card in self.cards:
            self.sum+=card.value
        
        #Attribute for showing dealer sum and card
        self.dealer_card = cards[0].name
        self.dealer_sum = cards[0].value
        
        #Counting aces within the hand
        self.aces_total = 0
        
    def __str__(self):
        names = []
        for card in self.cards:
            names.append(card.name)
        return ", ".join(names)
    
    def aces_check(self):
        self.aces_total = 0
        for card in self.cards:
            if card.name.split()[0] == "Ace":
                self.aces_total+=1
    
        #Reducing the sum of the hand depending on the number of aces in a player's hand
        if self.aces_total >= 1 and self.sum > 21:
            self.sum-=10*(self.aces_total)
            return True
            
class Chips():
    
    def __init__(self,amount):
        
        #Number of chips
        self.amount = amount
        
    def lose(self,chips):
        self.amount-=chips
    
    def win(self,chips):
        self.amount+=chips 
        
        
def display_hands():
    
    if player:
        titles = {"Dealer's Hand:":[Hand(dealer_hand).dealer_card], "Player's Hand:":[f"{player_turn}".strip()]}
        print(f"\n{DataFrame.to_string(DataFrame(titles), index = False, justify = 'left', col_space = 70)}")
        print("{0:69}  {1}".format(f" Value:  {Hand(dealer_hand).dealer_sum}", f" Value: {player_turn.sum}"))
        
    if dealer:
        titles = {"Dealer's Hand:":[dealer_turn], "Player's Hand:":[f"{player_turn}".strip()]}
        print(f"\n{DataFrame.to_string(DataFrame(titles), index = False, justify = 'left', col_space = 70)}")
        print("{0:69}  {1}".format(f" Value:  {dealer_turn.sum}", f" Value: {player_turn.sum}"))         
                
def replay():
    
    def off():
        global playing
        global player
        global dealer
        global win_cons
        global betting
        
        playing = False
        player = False
        betting = False
        dealer = False
        win_cons = False
    
    def game_on():
        global playing
        global dealer
        global win_cons
        global player
         
        playing = True    
        dealer = False
        win_cons = False
        player = False
        
    
    if player_chips.amount == 0:
        print("\nYou have run out of chips!\nGAME OVER!")
        off()

    else:
        while True:
            rep = input("\nWould you like to play again?: ")
            
            if len(rep) == 0:
                clear_output()
                print("\nPlease enter in something!")
                display_hands()
            
            elif rep.lower()[0] not in ("y","n"):
                clear_output()
                print("\nPlease enter in yes or no!")
                display_hands()
            
            elif rep.lower()[0] == "y":
                game_on()
                clear_output()
                break
            else:
                print("\nThanks for playing!")
                off()
                break
                

def player_fold():
    global betting
    global fold
    
    while True:
        fold = input("Would you like to fold this hand?: ")

        if len(fold) == 0:
            clear_output()
            print("\nPlease enter in a character!")                        

        elif fold.lower()[0] not in ("y","n"):
            clear_output()
            print("\nPlease enter in yes or no!")
            display_hands()

        elif fold.lower()[0] == "y":
            clear_output()
            print("\nThis hand has been folded!")
            display_hands()
            betting = False
            replay()
            break
        else:
            clear_output()
            break
            
                
def hit():
    global player
    global dealer
    global player_hand
    global fold
    
    if fold.lower()[0] == "y":
        player = False

    else:
        while True:
            display_hands()
            hit = input("\nWould you like to hit?: ")

            if len(hit) == 0:
                clear_output()
                print("You must enter in something!")

            elif hit.lower()[0] == "y":
                player_hand.append(the_deck.hit())
                clear_output()
                break

            elif hit.lower()[0] not in ("y","n"):
                clear_output()
                print("Please enter in yes or no!")

            else:
                clear_output()
                player = False
                dealer = True
                break
     
        
        
player_chips = Chips(100)
the_deck = Deck()

print("Hello, welcome to BlackJack!")

betting = True
playing = True
dealer = False
win_cons = False


while playing:
    player = True
    betting = True
    
    # Fold variable reset on each time a round commences
    fold = ' '
    
    print("\nShuffling the deck!")
    the_deck.shuffle()
    player_hand = the_deck.deal()
    dealer_hand = the_deck.deal()

    
    while player:
        player_turn = Hand(player_hand)
        
        while betting:
            # Will print the hand out to the console, takes into account whether or not to show one dealer card or two
            display_hands()
            print(f"\nYou have {player_chips.amount} chips.")

            try:
                bet = int(input("\nHow much would like to bet?: "))

            except:
                clear_output()
                print(f"\nPlease enter in a whole number that is less than {player_chips.amount}!")

            else:
                if bet == 0:
                    # Function giving the player the option to fold their current hand
                    player_fold()
                            
                elif bet > player_chips.amount:
                    clear_output()
                    print(f"\nYou don't have enough chips! Please enter an amount less than {player_chips.amount}!!")

                else:
                    clear_output()
                    print(f"\nYou have bet {bet} chips!\n{player_chips.amount - bet} remaining!")
                    betting = False
        
        if player_turn.aces_check():
            print("\nAs the player has an ace, and the hand is over 21, the sum has been reduced by 10!")

        if player_turn.sum > 21:
            display_hands()
            player_chips.lose(bet)
            print(f"\nPlayer has bust! \nYou have lost {bet} chips!\nYou have {player_chips.amount} chips remaining!")
            replay()
            break
        
        elif player_turn.sum == 21:
            display_hands()
            print("\nYou have scored 21 and won the hand!")
            win_cons = True
            break
        
        # Function that asks the player if they would like to hit
        hit()
        
    while dealer:
        dealer_turn = Hand(dealer_hand)
        
        if dealer_turn.aces_check():
            print("\nAs the dealer has an ace, and the hand is over 21, the sum has been reduced by 10!")
            
        display_hands()
        
        if dealer_turn.sum > 21:
            player_chips.win(bet)
            print(f"\nThe dealer has bust!\nYou have won {bet} chips!\nYou have {player_chips.amount} chips!")
            replay()
                         
        elif dealer_turn.sum == 21:
            print(f"\nThe dealer has a total of {dealer_turn.sum}!")
            dealer = False
            win_cons = True
            break
            
        elif dealer_turn.sum >= 18:
            dealer = False
            win_cons = True
            break            
        
        else:
            clear_output()
            dealer_hand.append(the_deck.hit())
            print("The dealer has hit!")
    
    while win_cons:
           
        if player_turn.sum == 21 or player_turn.sum > dealer_turn.sum:
            player_chips.win(bet)
            print(f"\nYou have won {bet} chips!\nYou have {player_chips.amount} chips!")
            
        
        elif player_turn.sum < dealer_turn.sum:
            player_chips.lose(bet)
            print(f"\nYou have lost {bet} chips!\nYou have {player_chips.amount} chips remaining!")
                
        
        elif player_turn.sum == dealer_turn.sum:
            print(f"\nTie game, your chips are returned!\nYou have {player_chips.amount} chips remaining!")

        replay()
        
