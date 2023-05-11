import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
                    #This needs to return the rnak of the car which will be passed to the hand class. Card.The_rank will be need to be called
    def __str__(self):
        return self.rank
   
class Deck:
    def __init__(self):  
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:      
                    created_card = Card(suit,rank)
                    self.all_cards.append(created_card)              
    def shuffle(self):
        random.shuffle(self.all_cards)  
    def deal_one(self):   
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0                    
    def add_card(self,new_cards):
        self.cards.append(new_cards)
        self.value += values[new_cards.rank]
    def adjust_for_ace(self):
        pass
    def __str__(self):
        return self.value

class Dealer_Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0                    
    def add_card(self,new_cards):
        self.cards.append(new_cards)
        self.value += values[new_cards.rank]
    def adjust_for_ace(self):
        pass
    def __str__(self):
        return self.value

class Chips:
    def __init__(self,player_bet):
        self.total=100
        self.bet=player_bet
    def win_bet(self):
        self.total+=self.bet
        return self.total
    def lose_bet(self):
        self.total-=self.bet
        return self.total
    def __str__(self):
        return f'Player has bet ${self.bet}'
        
new_deck=Deck()
new_deck.shuffle()
player_hand=Hand()
dealer_hand=Dealer_Hand()

player_bet = int(input("How much would you like to bet? "))
chips=Chips(player_bet)
print(chips)
print("PLAYER WALLET = ", chips.total)

#****DEALS INITAL 2 CARDS*******
for x in range(2):
    player_hand.add_card(new_deck.deal_one())
    dealer_hand.add_card(new_deck.deal_one())
print()
print('Player Card1- ',player_hand.cards[0])
print('Player Card2- ',player_hand.cards[1])
print('PLAYER TOTAL- ',player_hand.value)
print()
print('Dealer Card1- ',dealer_hand.cards[0])
print('Dealer Card2- ',dealer_hand.cards[1])
print('DEALER TOTAL-',dealer_hand.value)
print()

#***GAME LOGIC********
game_on = True
player_score=0
dealer_score=0

while game_on and player_hand.value<21:
    print("***********************************")
    player_choice = input("H = Hit OR S = Stay ")#*******BUILD TRY/CATCH LOGIC ERROR HANDLING NON INT INPUT
    
    if player_choice=="S":
        player_score+=player_hand.value
        print('PLAYER TOTAL- ',player_hand.value,'DEALER TOTAL- ', dealer_hand.value)
        game_on=False
        
        if player_hand.value>dealer_hand.value:
            print("PLAYER  WINS")
            chips.win_bet()
            print("PLAYER WALLET = ", chips.total)
        if player_hand.value<dealer_hand.value:
            print("DEALER WINS")
            chips.lose_bet()
            print("PLAYER WALLET = ", chips.total)
            
    if player_choice=="H":
        player_hand.add_card(new_deck.deal_one())
        dealer_hand.add_card(new_deck.deal_one())
        print('Drawn Player Card-- ',player_hand.cards[-1])
        print('PLAYER TOTAL- ',player_hand.value)
        player_score=player_hand.value
        print()
        print('Drawn Dealer Card--',dealer_hand.cards[-1])
        print('DEALER TOTAL - ',dealer_hand.value)
        
#******WIN / LOSE LOGIC****************        
        if player_hand.value>21:
            print("**PLAYER BUST**")
            game_on=False
            
        if dealer_hand.value>21:
            print("**DEALER BUST**")
            game_on=False
            
        elif dealer_hand.value and player_hand.value>21:
            print("BOTH BUST - DEALER WINS")
            break
    else:
        pass

          
#play_again = input("Would you like to play again? Y = YES, N=NO")
#if play_again=="Y":
#    game_on=True
#if play_again=="N":
#    print("Thank you for playing!")






