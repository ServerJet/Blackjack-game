## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# things needed:
#     UI
#     1.draw
#     2.show_draw_dealer
#     3.show_draw_player
#     3.count_player
#     4.count_dealer
#     5.compare
#     6.repeat

from calculator_art import logo
import random

#Adding a dictionary for the cards.
cards =  {
    'A' : 11,  
    2 : 2,    3 : 3,    4 : 4,
    5 : 5,    6 : 6,    7 : 7,
    8 : 8,    9 : 9,    10 : 10,
    'K' : 10,    'Q' : 10,  'J' : 10,  
}

#Function for drawing a new random card. 
def deal_card():
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J']
    deal = random.choice(cards)
    return deal

#Function to add the card to the existing hand.
def add_card(list):
    new_card = deal_card()
    list.append(new_card)

#Function to add the values of all the cards in a hand.
def add_hand(list):
    value = sum(list)
    if 11 in list:           #Checking if the 'A' should be counted a 1 or 11.
        if value > 21:
            value -= 10
            return value
        else:
            return value
    
    else:
        return value

#Function to give the cards its values.
def get_value(list):      
    new_list = []
    for card in list:
        for keys in cards:
            if keys == card:
                new_list.append(cards[keys])
                break
    return new_list

#Function to check for a blackjack.
def check_blackjack(list):
    if add_hand(list) == 21:        
        return True

user = []
user_value = []
dealer = []
dealer_value = [] 
    
print(logo)
print("\n-----------------Welcome to the game of Black Jack-----------------\n\n")

dealer.append(deal_card())
dealer.append(deal_card())
dealer_value = get_value(dealer)

user.append(deal_card())
user.append(deal_card())
user_value = get_value(user)
    
bigloop = True
   
print(f"Dealer :  [{dealer[0]}, #]")
print(f"dealer's first hand : {dealer_value[0]}")
if check_blackjack(dealer_value):
    print(f"The Dealer won the Blackjack!!  Their hand is {dealer}")
    bigloop = False


print(f"\nPlayer :  {user}")
print(f"user score : {add_hand(user_value)}")
if check_blackjack(user_value):
    print(f"The Player won the Blackjack!!  Their hand is {user}")
    bigloop = False
    

while bigloop is True:
    decision = input("1.Hit                    2.Stay\n")
    
    if  decision == "hit":
        add_card(user)
        print(f"\nPlayer :  {user}")
        user_value = get_value(user)
        print(f"user score : {add_hand(user_value)}")
        
        if add_hand(user_value) > 21:
            print("You went overboard!!! You loose!")
            print(f"Dealer's hand : {dealer}\nTheir score: {add_hand(dealer_value)}")
            bigloop = False
            
            
    elif decision == "stay":
        u_value = add_hand(user_value)
        d_value = add_hand(dealer_value)
        
        while add_hand(dealer_value) < 17:
            dealer.append(deal_card())
            dealer_value = get_value(dealer)
            
            if add_hand(dealer_value) > 21:
               
                d_value = add_hand(dealer_value)
                break
            
            elif add_hand(dealer_value) > 16:
                d_value = add_hand(dealer_value)
                break
            
            
        print(f"Dealer's hand : {dealer}\nTheir score: {add_hand(dealer_value)}")
        if u_value == d_value:
            print ("Draw!!")
            
        elif u_value > d_value:
            print ("You win!")
            
        elif u_value < d_value and d_value < 21: 
            print ("You loose!")
        
        elif d_value > 21:
            print("Dealer went overboard!!!\nYou win!")
        
        bigloop = False




# add_card(user)
# add_card(user)
# add_card(dealer)
# add_card(dealer)

# print(f"\nDealer :  [{dealer[0]}, #]")
# print(f"Player :  {user}")
# print(f"dealer score : {add_hand(dealer)}")
# print(f"user score : {add_hand(user)}")
