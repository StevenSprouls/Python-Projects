
import random
 
 
class Card():
 
    # Initialization of Card
    def __init__(self, card_num):
        card_dict = {1: "Ace", 2: "2", 3: "3", 4: "4",
                     5: "5", 6: "6", 7: "7", 8: "8",
                     9: "9", 10: "10", 11: "Jack",
                     12: "Queen", 13: "King"}
# Allows us to read suits in groups of thirteens easily
        card_num += 1
        if card_num >= 1 and card_num <= 13:
            self._card_suit = 'Spades'
        elif card_num > 13 and card_num <= 26:
            self._card_suit = 'Hearts'
        elif card_num > 26 and card_num <= 39:
            self._card_suit = 'Clubs'
        elif card_num > 39 and card_num <= 52:
            self._card_suit = 'Diamonds'
        else:
            print('Needs to be a card number from 0 to 51')
# Takes the card number and assigns the 1-13 value of the card
        if card_num > 39 and card_num <= 52:
            tempval = card_num - 39
        elif card_num > 26 and card_num <= 39:
            tempval = card_num - 26
        elif card_num > 13 and card_num <= 26:
            tempval = card_num - 13
        else:
            tempval = card_num
# Assigns the card's actual face value
        if tempval == 1:
            self._card_value = 11
        elif tempval >= 11:
            self._card_value = 10
        else:
            self._card_value = tempval
        self._card_rank = card_dict[tempval]
# Card is faced down by default
        self._card_isDown = True
 
# Returns the card's suit
    def get_suit(self):
        return self._card_suit
 
# Returns the card's rank
    def get_rank(self):
        return self._card_rank
 
# Returns the card's value
    def get_value(self):
        return self._card_value
 
# Faces the card down
    def face_down(self):
        self._card_isDown = True
 
# Faces the card up
    def face_up(self):
        self._card_isDown = False
 
# Prints the information of the card if the card is faced up
    def __str__(self):
        if self._card_isDown is False:
            return self.get_suit() + " is the suit. \n" + \
                   self.get_rank() + " is the cards rank. \n" + \
                   str(self.get_value()) + " is the card value. \n"
# Doesn't print card since it is faced down
        else:
            return "Please flip card over."
 
 
class ChipBank():
    # Initializes a chip bank
    def __init__(self, value):
        if type(value) == int:
            self._balance = int(value)
        else:
            print('Please enter an integer for the value.')
 
# Returns the amount asked
# or returns what's left and sets balance to 0
    def withdraw(self, amount):
        if amount > self._balance:
            amount = self._balance
            self._balance = 0
            return amount
        elif type(amount) == int:
            self._balance -= amount
            return amount
        else:
            print('Please enter an integer for the value.')
 
# Deposits the amount of chips
    def deposit(self, amount):
        if type(amount) == int:
            self._balance += amount
        else:
            print('Please enter an integer for the amount.')
 
# Returns balance
    def get_balance(self):
        return self._balance
 
# Prints the string of the chipbank object
    def __str__(self):
        # Setting balance to a variable name
        amount = self._balance
        og_amount = str(amount)
        # Getting black chips
        blackChips = str(amount // 100)
        amount = amount % 100
        # Getting green chips
        greenChips = str(amount // 25)
        amount = amount % 25
        # Getting red chips
        redChips = str(amount // 5)
        amount = amount % 5
        # Getting blue chips
        blueChips = str(amount)
        return 'Black Chips: ' + blackChips + '\n' + \
               'Green Chips: ' + greenChips + '\n' + \
               'Red Chips: ' + redChips + '\n' + \
               'Blue Chips: ' + blueChips + '\n' + \
               'Totaling $' + og_amount
 
 
# This is the test code in the lab assignment
def main():
    # ---------- For the card ----------
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        my_card.face_up()
        print(my_card)
    print(random.choice(deck))
    card = Card(37)
    print(card)
    print(card.get_value())
    print(card.get_suit())
    print(card.get_rank())
    card.face_down()
    print(card)
    card.face_up()
    print(card)
    # ------- For the chip bank ----------
    cs = ChipBank(149)
    print(cs)
    cs.deposit(7)
    print(cs.get_balance())
    print(cs)
    cs.deposit(120)
    print(cs)
    print(cs.withdraw(300))
    pass
 
# Calls main
if __name__ == '__main__':
    main()
