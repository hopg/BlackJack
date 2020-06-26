# BlackJack
### A BlackJack game using OOP with a simple betting functionality.

The game starts with asking the player how many chips they would like to bet; by default, the player starts with 100 chips.

Next, cards are then dealt to both the dealer and the player. The player can only see one of the dealer's cards and is asked whether they would like to hit, which is to add another card to their hand. The aim is for the player to achieve a hand value that is larger than the dealer's hand value and as close to 21 as possible without going over. 

The player can continue to hit until they choose not to or continue until they bust, that is, obtain a hand value over 21. If an Ace is drawn, for either the player or the dealer, and the sum of the hand is over 21, the value of the Ace becomes 1. The result is that the hand sum is reduced by 10 and there is no longer a bust. 

Once the player no longer continues to hit, the dealer's turn commences. The dealer will hit only if the sum of their hand is under 18 after which, they will stand. As a result, the dealer can still bust.

If the player wins the game, they win the amount of chips they bet.

The player can continue to play and accrue chips however, if the player runs out of chips then it results in game over. 

#### **Round end conditions:**
- The player obtains a perfect score of 21, the player will automatically win the round.
- The player's hand value is greater than the dealer's hand value, the player wins.
- The player and dealer tie, no chips are lost in this instance.
- The dealer busts.
- The dealer's hand value is greater than the player's hand value, the dealer wins.

#### **Required Modules:**
- random
- pandas (DataFrame)
- IPython.display (clear_output)

#### **Notes**:
- Can input "y"/"n" for any yes/no question, as a result, words starting with "y" or "n" will be passed through as yes or no respectively.
- Currently if the player is lucky enough to draw a 21, the player will still be able to place a bet and can effectively bet all their chips with 100% certainty of a win. 
