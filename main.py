import random

no_of_scenarios = 100000

# function goes through a single scenario of drawing cards until desired card is drawn. 
# Then returns number of cards needed to achieve success in this scenario.

def draw_until_success(no_of_successess):   
    no_of_cards_drawn = 0
    no_of_cards_left = 99 - no_of_cards_drawn
    while True: 
        draw_card = random.randint(1,no_of_cards_left)
        no_of_cards_drawn +=1
        if draw_card <= no_of_successess:
            return no_of_cards_drawn

# function performs one simulation that consists of the number of single scenarios given in no_of_scenarios variable
# then returns number of drawn card that resulted with success

def simulate(no_of_card_type):
    return [draw_until_success(no_of_card_type) for each in range(no_of_scenarios)]

# function counts probability of single success for each possible number of draws 
# then returns dictionary with those probabilities

def count_probability(list_of_results):
    matrix_of_probability = {}
    for each in range(1,100):
        matrix_of_probability.update({each:list_of_results.count(each)/no_of_scenarios*100})
    return matrix_of_probability

# function counts probability for each card type in deck 
# then returns result of analysis (dictionary with the same keys as card types stated in deck)

def analyse_deck(deck):
    deck_analysis  = dict()
    for each_key in deck.keys():
        deck_analysis.update({each_key:count_probability(simulate(deck[each_key]))})
    return deck_analysis

class Deck():

    def __init__(self, **kwargs):
        
