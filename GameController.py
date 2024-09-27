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
        self.__player_has_split = False
        self.__dealer_has_split = False

    def __get_card(self):
        tmp = random.choice(list(self.__deck.keys()))
        obj = random.choice(self.__deck[tmp])
        self.__deck[tmp].remove(obj)
        return obj

    def __check_equal_cards(self, hand):
        print(f"> {hand[0]} vs. {hand[1]}")
        return hand[0]==hand[1]

    def start_game(self):
        # get initial two cards for the player
        self.__player_hands[1].append(self.__get_card())
        self.__player_hands[1].append(self.__get_card())

        # get initial two cards for the dealer
        self.__dealer_hands[1].append(self.__get_card())
        self.__dealer_hands[1].append(self.__get_card())

        # print status and start a round
        self.game_status()
        self.make_round()

    def game_status(self):
        """
        Prints Player and Dealer hands with the remaining cards available.
        :return: None
        """
        # print player hands
        if len (self.__player_hands[2]) > 0:
            print(f"Player hands: {self.__player_hands[1]}, {self.__player_hands[2]}")
        else:
            print(f"Player hand: {self.__player_hands[1]}")

        # print dealer hands
        if len (self.__dealer_hands[2]) > 0:
            print(f"Dealer hands: {self.__dealer_hands[1]}, {self.__dealer_hands[2]}")
        else:
            print(f"Dealer hand: {self.__dealer_hands[1]}")

        # print remaining deck
        print("")
        print("Remaining cards:")
        print(self.__deck)

    def make_round(self):
        if self.__first_round:
            if self.__check_equal_cards(self.__player_hands[1]):
                option = input(f"Player, do you want to split (Y/n): ")
                if option == "Y" or option == "":
                    print(f"Splitting hand.")

            else:
                print("no equal cards")
        return

    def select_player_options(self):
        return None

