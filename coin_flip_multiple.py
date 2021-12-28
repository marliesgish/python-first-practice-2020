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

        n = 0

        while True:
            try:
                answer = int(input("How often do you want to flip the coin?"))
            except ValueError:
                print("Your input is not valid, please insert a number")
                continue
            else:
                break

        while n < answer:
            coin = random.randint(0,1)
            if coin == 0:
                print("Heads")
                list_heads.append("Heads")
                n += 1
            else:
                print("Tails")
                list_tails.append("Tails")
                n += 1

        self.get_printed_information(list_heads, list_tails)
    

    def get_printed_information(self, list_heads, list_tails):
        len_heads_tails = [len(list_heads), len(list_tails)]

        heads_tails_p_s = self.get_plural_singular(len_heads_tails)

        print(f"\nTotal Heads or Tails:")
        print(f"Heads: {len_heads_tails[0]} {heads_tails_p_s[0]}")
        print(f"Tails: {len_heads_tails[1]} {heads_tails_p_s[1]}")


    def get_plural_singular(self, len_heads_tails):

        heads_tails_p_s = []

        for len_h_t in len_heads_tails:
            if len_h_t > 1:
                len_h_t = "times"
                heads_tails_p_s.append(len_h_t)
            else:
                len_h_t = "time"
                heads_tails_p_s.append(len_h_t)

        return heads_tails_p_s


person1 = Coins()
