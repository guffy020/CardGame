from deck import Deck
from card import Card
import code


print("This is Slapjack between player1 and player2. Hit -ENTER- to genorate a random card. When a jack appers player1 hit -A- player2 hit -K- first person to hit it wins the round. first player to win 2 rounds wins the game")

winnumber = 2
player1win = 0
player2win = 0


gamedeck = Deck()
gamedeck.Shuffle()
currentcard = gamedeck.TakeFromTop ()

JackofClubs = Card("Jack","Clubs")
JackofSpades = Card("Jack","Spades")
JackofDiamonds = Card("Jack","Diamonds")
JackofHearts = Card("Jack","Hearts")


while(currentcard != JackofClubs and currentcard != JackofSpades and currentcard != JackofDiamonds and currentcard != JackofHearts):
    print("press enter for new card")
    g =raw_input()
    currentcard = gamedeck.TakeFromTop ()
    currentcard. displayCard()
    if(currentcard == JackofClubs or currentcard == JackofSpades or currentcard == JackofDiamonds or currentcard == JackofHearts):
        print("A jack has been found") 
        key =code.guffyInput()
        #key =str(key)
        if(key == "a"):
            print("player 1 won the round")
            player1win += 1
        if(key == "k"):
            print("player 2 won the round")
            player2win += 1
    if(player1win == winnumber):
        print("congrats player 1 won the slap jack game")
    if(player2win == winnumber):
        print("Congrats player 2 won the slap jack game")
    if(player1win == 2 or player2win == 2):
        break