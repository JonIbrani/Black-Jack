
import random

player = True
dealer = True

the_deck_of_cards = [2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,
'Jack','King','Queen','Ace','Jack','King','Queen','Ace']

the_players_hand = []
the_dealers_hand = []

def Deal_the_Cards(round):
    random_numbers = random.randint(0,len(the_deck_of_cards) - 1)
    random_cards = the_deck_of_cards[random_numbers]
    round.append(random_cards)
    the_deck_of_cards.remove(random_cards)

def total_score(round):
    ace_11s = 0
    total = 0
    royal_cards = ['King','Jack','Queen']
    for random_card in round:
        if random_card in range(1,11):
            total += random_card
        elif random_card in royal_cards:
            total +=10
        else:
            total += 11
            ace_11s +=1
    while ace_11s and total >21:
        total -= 10
        ace_11s -= 1
    return total
        
        
def reveal_dealer_hand():
    if len(the_dealers_hand) == 2:
        return the_dealers_hand[0]
    elif len(the_dealers_hand) > 2:
        return the_dealers_hand[0]

for element in range(2):
    Deal_the_Cards(the_dealers_hand)
    Deal_the_Cards(the_players_hand)


while player or dealer:
    print(f'Dealer has {reveal_dealer_hand()} and X')
    print(f'Your hand is {the_players_hand} for a total score of {total_score(the_players_hand)}')
    if player:
        stay_or_hit = input('Press "S" to stay or press "H" to hit.')
    if total_score(the_dealers_hand) > 17:
        dealer = False
    else:
        Deal_the_Cards(the_dealers_hand)
    if stay_or_hit == "S":
        player = False
    else:
        Deal_the_Cards(the_players_hand)
    if total_score(the_players_hand) >= 21:
        break
    elif total_score(the_dealers_hand) >= 21:
        break

if total_score(the_players_hand) == 21 and total_score(the_dealers_hand) != 21:
    print(f'Your hand is {the_players_hand} for a total score {total_score(the_players_hand)} and the dealer hand is {the_dealers_hand} for a total score of {total_score(the_dealers_hand)}')
    print("Black Jack! The dealer lost. You are the winner")

elif total_score(the_dealers_hand) == 21 and total_score(the_players_hand) != 21:
    print(f'Your hand is {the_players_hand} for a total score {total_score(the_players_hand)} and the dealer hand is {the_dealers_hand} for a total score of {total_score(the_dealers_hand)}')
    print('Black Jack! The dealer wins. You lose.')


elif total_score(the_players_hand) > 21:
    print(f'Your hand is {the_players_hand} for a total score {total_score(the_players_hand)} and the dealer hand is {the_dealers_hand} for a total score of {total_score(the_dealers_hand)}')
    print('You have busted. The dealer wins!')

elif total_score(the_dealers_hand) > 21:
    print(f'Your hand is {the_players_hand} for a total score {total_score(the_players_hand)} and the dealer hand is {the_dealers_hand} for a total score of {total_score(the_dealers_hand)}')
    print('The dealer has busted. You win!')

elif 21 - total_score(the_dealers_hand) < 21 - total_score(the_players_hand):
    print(f'Your hand is {the_players_hand} for a total score {total_score(the_players_hand)} and the dealer hand is {the_dealers_hand} for a total score of {total_score(the_dealers_hand)}')
    print('The dealer wins!')

elif 21 - total_score(the_dealers_hand) > 21 - total_score(the_players_hand):
    print(f'Your hand is {the_players_hand} for a total score {total_score(the_players_hand)} and the dealer hand is {the_dealers_hand} for a total score of {total_score(the_dealers_hand)}')
    print('You win!')