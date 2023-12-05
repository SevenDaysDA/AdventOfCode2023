# Open the file
# file_path = 'solutions/aoc_4/test_data.txt' 
file_path = 'solutions/aoc_4/data_cards.txt' 


cards = []

with open(file_path, 'r') as file:
    # Read each line
    for line in file:
        # Split the line based on '|'
        # import ipdb; ipdb.set_trace()
        left, right = line.strip().split(":")[1].split('|')
        
        # Process the left and right sides
        winning_numbers = list(map(int, left.strip().split()))
        candidates = list(map(int, right.strip().split()))
        cards.append((winning_numbers, candidates))

print(cards)
total_score = 0

for card in cards:
    winning, candidates = card

    card_score = 0
    matches = 0

    for c_id , c in enumerate(candidates):
        if c in winning:
            matches += 1
    
    if matches == 0:
        card_score = 0
    elif matches == 1:
        card_score = 1
    else:
        card_score = 2**(matches - 1)

    print(card_score)
    total_score += card_score
print(total_score)
    # for c_id , c in enumerate(candidates):
    #     if c_id == 0:
    #         if c in winning:
    #             doubled = True

    #     if c in winning:
    #         card_score += 1
    # if doubled:
    #     card_score *= 2

    # for c_id , c in enumerate(candidates):
    #     if c in winning and consecutive:
    #         card_score += 2
    #     elif c in winning:
    #         card_score += 1
    #     else:
    #         # No card score addition
    #         consecutive = False

