import random

class GameController:

    def __init__(self):
        self.player_hands = {
            1: [],
            2: []
        }
        self.dealer_hands = {
            1: [],
            2: []
        }
        self.cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
        self.deck = {
            "spades": self.cards[:],
            "hearts": self.cards[:],
            "diamonds": self.cards[:],
            "clubs": self.cards[:]
        }
        self.first_round = True

    def __get_card(self):
        tmp = random.choice(list(self.deck.keys()))
        obj = random.choice(self.deck[tmp])
        self.deck[tmp].remove(obj)
        return obj


    def start_game(self):
        self.player_hands[1].append(self.__get_card())
        self.player_hands[1].append(self.__get_card())
        self.dealer_hands[1].append(self.__get_card())
        self.dealer_hands[1].append(self.__get_card())


    def game_status(self):
        print(f" Table cards:")

        # print player hands
        print(f" Player: ")
        for hand in self.player_hands.keys():
            print(self.player_hands[hand])

        # print dealer hands
        print(f" Dealer: ")
        for hand in self.dealer_hands.keys():
            print(self.dealer_hands[hand])
        print("")

        # print remaining deck
        print("Remaining cards:")
        for brand in self.deck.keys():
            print(f"{brand}: {self.deck[brand]}")


    def select_player_options(self):
        return None

