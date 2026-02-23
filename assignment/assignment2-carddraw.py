import requests
from collections import Counter

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=5"

#testing the api
#print("This is the dealcards.py file.")

#GET request to shuffle the deck and check the response
response = requests.get(url)

#Shuffle the deck and get the deck id from the response
shuffled_deck = response.json()
deck_id = shuffled_deck['deck_id']
#print(response.text)
#print("The deck id is: " + deck_id)

#GET request to draw 5 cards from the shuffled deck and check the response
shuffled_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=5"
response_shuffle = requests.get(shuffled_url)
#print(response_shuffle.text)

#Parse the response to get the cards drawn and print them out
response_shuffle_json = response_shuffle.json()
cards = response_shuffle_json['cards']
#print("The cards drawn are: ")

#Function to convert the card value to a number for easier comparison
def card_to_number(card):
    values = {
    "ACE": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "JACK": 11,
    "QUEEN": 12,
    "KING": 13
    }
    return values[card]

#Create a function to check if the cards drawn form a straight (5 cards in a row)
def is_straight(numbers):
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) != 5:
        return False
    low_ace_straight = set([1, 2, 3, 4, 5])
    high_ace_straight = set([10, 11, 12, 13, 1])
    normal_straight = unique_numbers[-1] - unique_numbers[0] == 4
    return low_ace_straight or high_ace_straight or normal_straight

card_numbers = [card_to_number(card['value']) for card in cards]
value_counts = Counter(card_numbers)

has_pair = any(count == 2 for count in value_counts.values())
has_triple = any(count == 3 for count in value_counts.values())
has_straight = is_straight(card_numbers)

#Loop through the cards and print out the value and suit of each card
for card in cards:
    value = card_to_number(card['value'])
    #print the original value/numeric and the suit of the card
    print("Card: " + card['value'] + " of " + card['suit'] + " (Numeric value: " + str(value) + ")")
    
print(f"pair={has_pair},triple={has_triple},straight={has_straight}")

if has_pair:
    print("You have a pair!")
elif has_triple:
    print("You have a triple!")
elif has_straight:
    print("You have a straight!")
else:
    print("You do not have any combination.")