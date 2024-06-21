deck = input().split(' ')
shuffles = int(input())

for shuffle in range(shuffles):
    new_deck = []
    deck_a = deck[:int(len(deck)/2):]
    deck_b = deck[int(len(deck)/2)::]
    for card in range(len(deck_a)):
        new_deck.append(deck_a[card])
        new_deck.append(deck_b[card])
    deck = new_deck

print(deck)
