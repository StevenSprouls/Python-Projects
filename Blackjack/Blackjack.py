
class BlackjackHand:
    # Creates Hand List
    def __init__(self):
        self.hand = []

# Adds card to hand

    def add_card(self, new_card):
        self.hand.append(new_card)

# Prints Cards as a string

    def __str__(self):
        cards = ""
        for card in self.hand:
            cards += str(card) + ", "
        return cards[:-2]

# Gets Card Values

    def get_value(self):
        self.value = 0
        for card in self.hand:
            self.value += card.get_value()
        if self.value > 21:
            for card in self.hand:
                if card.get_rank() == "Ace":
                    self.value -= 10
        return self.value


class Blackjack:
    # Creates Deck
    def __init__(self, starting_dollars):
        self.deck = []
        for i in range(52):
            card = Card(i)
            card.face_up()
            self.deck.append(card)
        shuffle(self.deck)
        self.bank = ChipBank(starting_dollars)

# Draws Card from deck

    def draw(self):
        if self.deck == []:
            for i in range(52):
                card = Card(i)
                card.face_up()
                self.deck.append(card)
            shuffle(self.deck)
        else:
            self.x = self.deck[0]
            self.deck.remove(self.deck[0])
        return self.x

# Creates hands for both the player and the dealer.

    def start_hand(self, wager):
        self.playerHand = BlackjackHand()
        self.dealerHand = BlackjackHand()
        self.wager = wager
        for i in range(2):
            x = self.draw()
            self.playerHand.add_card(x)
            self.y = self.draw()
            if i == 0:
                self.y.face_down()
            self.dealerHand.add_card(self.y)
# Prints hands for both dealer and player
        print("Your starting hand: " + str(self.playerHand))
        print("Dealer's starting hand: " + str(self.dealerHand))
        if (self.playerHand.get_value() == 21 and
                self.dealerHand.get_value() != 21):
            self.end_hand("win")
        elif (self.playerHand.get_value() == 21 and
              self.dealerHand.get_value() == 21):
            self.end_hand("push")
        self.bank.withdraw(self.wager)

# Hits the deck if player decides to hit.

    def hit(self):

        x = self.draw()
        print("You draw: " + str(x))
        self.playerHand.add_card(x)
        print("Your hand is now: " + str(self.playerHand))
        if self.playerHand.get_value() == 21:
            self.stand()
        elif self.playerHand.get_value() > 21:
            print("You bust!")
            self.end_hand("lose")

# Gives the option for the player to stand

    def stand(self):

        self.dealerHand.hand[0].face_up()
        print("Dealer's hand is now: " + str(self.dealerHand))
        while self.dealerHand.get_value() <= 16:
            x = self.draw()
            print("Dealer draws: " + str(x))
            self.dealerHand.add_card(x)
            print("Dealer's hand is now: " + str(self.dealerHand))
        if self.dealerHand.get_value() > 21:
            self.end_hand("win")
            print("Dealer bust, you win!")
        elif self.playerHand.get_value() > self.dealerHand.get_value():
            self.end_hand("win")
            print("You beat dealer's hand!")
        elif self.playerHand.get_value() < self.dealerHand.get_value():
            self.end_hand("lose")
            print("Dealer beats your hand!")
        elif self.playerHand.get_value() == self.dealerHand.get_value():
            self.end_hand("push")
            print("Push!")

# Returns the outcome strings of the hands.

    def end_hand(self, outcome):

        if outcome.lower() == "win":
            self.bank.deposit(self.wager * 2)
        elif outcome.lower() == "push":
            self.bank.deposit(self.wager)
        elif outcome.lower() == "lose":
            self.bank.deposit(0)
        self.playerHand = None
        self.playerHand = None

# Returns true or false if a game is happening.
    def game_active(self):

        if self.playerHand is None:
            return False
        else:
            return True
# Provided sample code
if __name__ == "__main__":
    blackjack = Blackjack(250)
    while blackjack.bank.get_balance() > 0:
        print("Your remaining chips: " + str(blackjack.bank))
        wager = int(input("How much would you like to wager? "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print()
    print("Out of money! The casino wins!")
