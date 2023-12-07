

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
        return card1
    elif card1_value > card2_value:
        return card2
    else:
        return 0



score_ranks= {"Five1":6,"Four1":5,"FullH":4,"Thre1":3,"Two2":2,"One1":1,"High":0}

def Evaluate_Hand(hand):
    