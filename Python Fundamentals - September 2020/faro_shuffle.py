cards = input().split(" ")
num_shuffle = int(input())

half = len(cards) // 2

top_card = cards[0]
bottom_card = cards[-1]

shuffle_cards = []
left_side = []
right_side = []
for num_shuffle in range(num_shuffle):
    left_side = []
    right_side = []

    for i in range(1, half):
        left_side.append(cards[i])

    for j in range(half, len(cards) - 1):
        right_side.append(cards[j])

    for index in range(len(left_side)):
        shuffle_cards.append(right_side[index])
        shuffle_cards.append(left_side[index])

    cards = shuffle_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffle_cards = []
print(cards)
