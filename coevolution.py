import random
import matplotlib.pyplot as plt

# 0 = hearts
# 1 = diamonds
# 2 = clubs
# 3 = spades

class Deck:
    """
    Simplified representation of a deck of cards. Only count of each suit in deck is maintained.

    Attributes:
        suit_counts: List of length 4, each element counts the number of each suit - hearts, diamonds, clubs, and spades respectively
    """
    def __init__(self, suit_counts=None) -> None:
        if suit_counts is None:
            self.suit_counts = [13, 13, 13, 13]
        else:
            self.suit_counts = suit_counts
    
    def get_card_count(self):
        return sum(self.suit_counts)

    def pick_card(self, random_suit=True, chosen_suit=None):
        if random_suit:
            while True:
                suit = random.randint(0, 3)
                if self.suit_counts[suit] != 0:
                    break
            self.suit_counts[suit] -= 1
            return suit
        else:
            if self.suit_counts[chosen_suit] == 0:
                print("None of suit left in deck")
                return None
            else:
                self.suit_counts[chosen_suit] -= 1
                return chosen_suit
    
    def add_card(self, suit):
        self.suit_counts[suit] += 1

    def combine_deck(self, other_deck):
        for suit in range(4):
            for i in range(other_deck.suit_counts[suit]):
                self.add_card(suit)
        other_deck.suit_counts = [0, 0, 0, 0]


class Evolution:
    """
    Simulate coevolution card game.

    Attributes:
        host_deck: Reserve deck for host
        para_deck: Reserve deck for parasite
        host_hand: Cards to be included in "competition" for host
        para_hand: Cards to be included in "competition" for parasite
    """
    def __init__(self) -> None:
        self.host_deck = Deck()
        self.para_deck = Deck()
        self.host_hand = self.initialise_hand(self.host_deck)
        self.para_hand = self.initialise_hand(self.para_deck)

    def initialise_hand(self, deck):
        hand = Deck(suit_counts=[0, 0, 0, 0])
        for i in range(12):
            suit = deck.pick_card()
            hand.add_card(suit)
        return hand
    
    def simulate_encounters(self):
        host_live_pile = Deck([0,0,0,0])
        host_die_pile = Deck([0,0,0,0])
        para_live_pile = Deck([0,0,0,0])
        para_die_pile = Deck([0,0,0,0])
        for i in range(12):
            host_instance = self.host_hand.pick_card()
            para_instance = self.para_hand.pick_card()
            if host_instance != para_instance:
                # Host lives, parasite dies
                host_live_pile.add_card(host_instance)
                para_die_pile.add_card(para_instance)
            else:
                # Host dies, parasite lives
                host_die_pile.add_card(host_instance)
                para_live_pile.add_card(para_instance)
        return host_live_pile, host_die_pile, para_live_pile, para_die_pile
     
    def reproduction(self, live_pile, die_pile, host=True):
        temp_pile = Deck([0,0,0,0])
        if host:
            self.host_deck.combine_deck(die_pile)
            for suit in range(4):
                for count in range(live_pile.suit_counts[suit]):
                    if self.host_deck.suit_counts[suit] != 0:
                        self.host_deck.pick_card(random_suit=False, chosen_suit=suit)
                        temp_pile.add_card(suit)
                    else:
                        rand_card = self.host_deck.pick_card()
                        temp_pile.add_card(rand_card)
            live_pile.combine_deck(temp_pile)
            while live_pile.get_card_count() > 12:
                self.host_deck.add_card(live_pile.pick_card())
            while live_pile.get_card_count() < 12:
                live_pile.add_card(self.host_deck.pick_card())
            return live_pile
        else:
            self.para_deck.combine_deck(die_pile)
            for suit in range(4):
                for count in range(live_pile.suit_counts[suit]):
                    if self.para_deck.suit_counts[suit] > 1:
                        for child in range(2):
                            self.para_deck.pick_card(random_suit=False, chosen_suit=suit)
                            temp_pile.add_card(suit)
                    elif self.para_deck.suit_counts[suit] == 1:
                        self.para_deck.pick_card(random_suit=False, chosen_suit=suit)
                        temp_pile.add_card(suit)
                        temp_pile.add_card(self.para_deck.pick_card())
                    elif self.para_deck.suit_counts[suit] == 0:
                        for child in range(2):
                            temp_pile.add_card(self.para_deck.pick_card())
            live_pile.combine_deck(temp_pile)
            while live_pile.get_card_count() > 12:
                self.para_deck.add_card(live_pile.pick_card())
            while live_pile.get_card_count() < 12:
                live_pile.add_card(self.para_deck.pick_card())
            return live_pile
                    
    def run_evolution(self, num_runs, host_starting_hand=None, para_starting_hand=None):
        if host_starting_hand is not None:
            self.host_hand.suit_counts = host_starting_hand[:]
        if para_starting_hand is not None:
            self.para_hand.suit_counts = para_starting_hand[:]
        yield self.host_hand.suit_counts, self.para_hand.suit_counts
        for i in range(num_runs):
            host_live_pile, host_die_pile, para_live_pile, para_die_pile = self.simulate_encounters()
            self.host_hand = self.reproduction(host_live_pile, host_die_pile)
            self.para_hand = self.reproduction(para_live_pile, para_die_pile, host=False)
            yield self.host_hand.suit_counts, self.para_hand.suit_counts





