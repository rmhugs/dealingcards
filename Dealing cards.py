"from __future__ import division"

import random

def deal_hand(hands=1, cards=5):

	def create_deck():
		# create list of faces and suits
		deck_faces = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		deck_suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
		deck = []
		# create cards and add to deck
		for suit in deck_suits:

			for face in deck_faces:
				card = face + " of " + suit
				deck.append(card)
		# assert that there is 1 of each card in the deck and 52 cards
		for card in deck:
			assert deck.count(card) == 1
		assert len(deck) == 52
		# return deck
		return deck

	deck = create_deck()
	saved_hands = open('saved_hands.txt', 'w')\

	# deal hands
	for card in range(0, hands):
		hand = []

		# deal cards
		for card_number in range(0, cards):

			# if the deck has run out add another deck
			if len(deck) == 0:
				deck = create_deck()
				assert len(deck) == 52

			# shuffle deck, take first card, and remove
			random.shuffle(deck)
			hand.append(deck[0])
			deck.remove(deck[0])

		# check size of hand is correct
		assert len(hand) == cards

		# remove [], '
		for item in ['[', ']', "'"]:
			hand = str(hand).replace(item, '')
		# save to file
		saved_hands.write(str(hand) + '\n')

	# close file
	saved_hands.close()


def count_same_suits():

	saved_hands = open("saved_hands.txt").readlines()

	same_suit = []

	# count suits in hand
	for line in saved_hands:
		spades_count = line.count('Spades')
		hearts_count =line.count('Hearts')
		diamonds_count = line.count('Diamonds')
		clubs_count = line.count('Clubs')

		# if all are the same suit, add to same_suit list
		if (spades_count or hearts_count or diamonds_count or clubs_count) == 5:
			same_suit.append(line)
		
	return len(same_suit)

	saved_hands.close()



# deal a number of decks, count same suits and add to list
no_same_suits = []
for multiply in range(0,50):
	deal_hand(1000)
	same_suits = count_same_suits()
	no_same_suits.append(same_suits)

total = 0
for value in no_same_suits:
	total = total + value

print (total)

mean = total / len(no_same_suits)
print (mean)

