import random

class GameController:

    def __init__(self):
        self.__player_hands = {
            1: [],
            2: []
        }
        self.__dealer_hands = {
            1: [],
            2: []
        }
        self.__cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
        self.__deck = {
            "spades": self.__cards[:],
            "hearts": self.__cards[:],
            "diamonds": self.__cards[:],
            "clubs": self.__cards[:]
        }
        self.__first_round = True

    def __get_card(self):
        tmp = random.choice(list(self.__deck.keys()))
        obj = random.choice(self.__deck[tmp])
        self.__deck[tmp].remove(obj)
        return obj

    def __check_equal_cards(self, hand):
        print(f"> {hand[0]} vs. {hand[1]}")
        return hand[0]==hand[1]

    def start_game(self):
        self.__player_hands[1].append(self.__get_card())
        self.__player_hands[1].append(self.__get_card())
        self.__dealer_hands[1].append(self.__get_card())
        self.__dealer_hands[1].append(self.__get_card())
        self.game_status()
        self.make_round()

    def game_status(self):
        print(f" Table cards:")

        # print player hands
        print(f" Player: ")
        for hand in self.__player_hands.keys():
            print(self.__player_hands[hand])

        # print dealer hands
        print(f" Dealer: ")
        for hand in self.__dealer_hands.keys():
            print(self.__dealer_hands[hand])
        print("")

        # print remaining deck
        print("Remaining cards:")
        print(self.__deck)

    def make_round(self):
        if self.__first_round==True:
            if self.__check_equal_cards(self.__player_hands[1]):
                print(f"equal cards")
            else:
                print("no equal cards")
        return

    def select_player_options(self):
        return None

