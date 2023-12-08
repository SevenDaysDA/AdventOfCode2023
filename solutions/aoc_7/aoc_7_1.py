

point_ranks = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7, "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2":0}


def card_value(card):
    return point_ranks.get(card)

def Compare_Cards(card1, card2):
    """
        Return card name or 0 (if equal)
    """
    card1_value = card_value(card1)
    card2_value = card_value(card2)

    if card1_value > card2_value:
        return 1
    elif card1_value > card2_value:
        return 2
    else:
        return 0



score_ranks= {"Five1":6,"Four1":5,"FullH":4,"Thre1":3,"Two2":2,"One1":1,"High":0}


def read_txt(filename):
    cards = []
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Process each line (here, you can do whatever you want with the line)
            card, score = line.strip().split(" ")  
            cards.append((card, int(score)))
    print(cards)

read_txt("solutions/aoc_7/input_test.txt")



def is_Five1(hand):
    for card in point_ranks.keys():
        if 
# def is_Four1(hand):

# def is_FullH(hand):    


# def generic_value_hand(hand):

#     for card in hand:



# def Evaluate_Hand(hand1, hand2):

    