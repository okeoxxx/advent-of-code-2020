import copy
from pprint import pprint
from collections import deque
from data import inputGen

f = inputGen.getPuzzle(2020, 22)
file = f.input_data
file = file.split('\n')

deck1 = []
deck2 = []
filling_deck_2 = False
file.pop(0)
while file:
    n = file.pop(0)
    if n == '':
        filling_deck_2 = True
        file.pop(0)
    elif filling_deck_2:
        deck2.append(int(n))
    else:
        deck1.append(int(n))

def find_winner(deck1, deck2, part2=False):
    previous = set()
    while deck1 and deck2:
        winner = False
        board = ','.join(map(str, deck1)) + '+' + ','.join(map(str, deck2))
        if board in previous:
            return 1, 0
        else:
            previous.add(board)
        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if len(deck1) >= card1 and len(deck2) >= card2 and part2 == True:
            try:
                winner, _ = find_winner(deque(list(deck1)[:card1]), deque(list(deck2)[:card2]), part2=True)
            except:
                print(card1, deck1)
                print(card2, deck2)
                quit()
            if winner == 1:
                winning_deck, winning_card, loosing_card = deck1, card1, card2
            else:
                winning_deck, winning_card, loosing_card = deck2, card2, card1
        else:
            if card1 > card2:
                winning_deck, winning_card, loosing_card = deck1, card1, card2
            elif card1 < card2:
                winning_deck, winning_card, loosing_card = deck2, card2, card1
        winning_deck.append(winning_card)
        winning_deck.append(loosing_card)
    winner = 1 if deck1 else 2
    return winner, winning_deck

def get_result(deck1, deck2, part):
    if part == 1:
        _, winning_deck = find_winner(deque(copy.deepcopy(deck1)), deque(copy.deepcopy(deck2)), part2=False)
    else:
        _, winning_deck = find_winner(deque(copy.deepcopy(deck1)), deque(copy.deepcopy(deck2)), part2=True)
    result = 0
    for point, num in enumerate(reversed(winning_deck), 1):
        result += point * num
    return result

result1 = get_result(deck1, deck2, 1)
result2 = get_result(deck1, deck2, 2)

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
