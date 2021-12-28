'''
Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
'''

import random


class Coins():

    def __init__(self):
        self.start()

    def start(self):
        list_heads = []
        list_tails = []

        while True:
            try:
                answer = input("Do you want to flip the coin? (y/n)")
            except ValueError:
                print("Your input is not valid, please insert 'y' or 'n'")
            else:
                if answer.lower() == "y":
                    coin = random.randint(0, 1)
                    if coin == 0:
                        print("Heads")
                        list_heads.append("Heads")
                    else:
                        print("Tails")
                        list_tails.append("Tails")
                elif answer.lower() == "n":
                    self.get_printed_information(list_heads, list_tails)
                    break
                else:
                    print("Your input is not valid, please insert 'y' or 'n'")

    def get_printed_information(self, list_heads, list_tails):
        len_heads = len(list_heads)
        len_tails = len(list_tails)

        heads_p_s, tails_p_s = self.get_plural_singular(len_heads, len_tails)

        print(f"\nTotal Heads or Tails:")
        print(f"Heads: {len_heads} {heads_p_s}")
        print(f"Tails: {len_tails} {tails_p_s}")

    def get_plural_singular(self, len_heads, len_tails):

        if len_heads > 1:
            heads_p_s = "times"
        else:
            heads_p_s = "time"

        if len_tails > 1:
            tails_p_s = "times"
        else:
            tails_p_s = "time"

        return heads_p_s, tails_p_s


person1 = Coins()
