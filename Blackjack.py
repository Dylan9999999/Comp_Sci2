import random #imports a random dictionary

# Initialize deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] #creates a list of suits in a card deck
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'] #creates a list of ranks or cards in a card deck
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}#creates a list of values for each rank or card in the deck

# Functions
def deal_card(): #creates a function which picks a radnom suit and card
    suit = random.choice(suits) #picks a random suit from the list of suits
    rank = random.choice(ranks)#picks a rank from the list of ranks
    return (rank, suit)#returns the random suit and rank picked

def calculate_hand_value(hand): #creates a function which values the sum of the hand
    value = sum([values[card[0]] for card in hand]) #calculates the sum of the vaules in the hand
    num_aces = sum([1 for card in hand if card[0] == 'Ace']) #calculates the number of aces
    
    while value > 21 and num_aces: #runs this when the variable value is greater than 21 and there is an ace 
        value -= 10 #subtracts 10 from the value of the ace
        num_aces -= 1 #subtracts one from the variable of num_aces
    
    return value #returns the value

# Game setup
player_hand = [deal_card(), deal_card()]#runs the function deal_card two times and sets the player hand equal to it
dealer_hand = [deal_card(), deal_card()]#runs the function deal_card two times and sets the dealer hand equal to it

# Game loop
while True: #creates a while loop
    player_value = calculate_hand_value(player_hand)#sets the player_value equal to the value of the players hand
    dealer_value = calculate_hand_value(dealer_hand)#sets the dealer_value equal to the value of the dealers hand
    
    print("\nYour hand:", player_hand, "Value:", player_value) #print the players hand followed by their value
    print("Dealer's hand:", [dealer_hand[0], 'Hidden']) #prints one of the dealers cards and hides the other
    
    if player_value == 21: #if the players value is 21
        print("Blackjack! You win!") #prints "Blackjack! You win!"
        break#end the loop
    elif player_value > 21: #if the players value goes over 21
        print("Bust! You lose.")# print Bust! You lose
        break #end the loop
    
    action = input("Do you want to 'hit' or 'stand'? ").lower()#asks the user if they want to hit or stand
    
    if action == 'hit': #if the user responds hit
        player_hand.append(deal_card())#adds another card to the players hand using the dealcard function
    elif action == 'stand': #if the user answers stand
        while dealer_value < 17: #when the dealer value is under 17
            dealer_hand.append(deal_card()) #add another card to the dealers hand
            dealer_value = calculate_hand_value(dealer_hand) #calculate the value of the dealers hand
        
        print("Dealer's hand:", dealer_hand, "Value:", dealer_value) #print the dealers hand value
        
        if dealer_value > 21 or player_value > dealer_value: #if the player value is greater then dealer value or the dealer value is over 21
            print("You win!") #print you win
        elif dealer_value > player_value: #if the dealer value is higher then player value
            print("Dealer wins.") #print dealer wins
        else:#anything else
            print("It's a tie!") #print its a tie
        
        break#end the loop