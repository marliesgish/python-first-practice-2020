'''
The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
'''

import math


class ChangeReturn():


    def __init__(self):
        self.cost, self.money_given = self.get_amount_change()
        self.change_money()


    def get_amount_change(self):
        while True:
            try:
                cost = float(input("Please enter the total cost of your purchase"))
            except ValueError:
                print("Your input is not valid, please try again")
            else:
                break

        while True:
            try:
                money_given = float(input("Please enter the amount of cash that you give"))
            except ValueError:
                print("Your input is not valid, please try again")
                continue
            else:
                if money_given < cost:
                    print("The given money is not enough")
                    continue
                else:
                    break

        return float(cost), float(money_given)


    def change_money(self):
        cost = self.cost
        money_given = self.money_given
        change = money_given-cost

        money = [
            {
                "amount": 50,
                "amount_2": 50,
                "money_type": 'bill'
            },
            {
                "amount": 20,
                "amount_2": 50,
                "money_type": 'bill'
            },
            {
                "amount": 10,
                "amount_2": 10,
                "money_type": 'bill'
            },
            {
                "amount": 5,
                "amount_2": 5,
                "money_type": 'bill'
            },
            {
                "amount": 2,
                "amount_2": 2,
                "money_type": 'coin'
            },
            {
                "amount": 1,
                "amount_2": 1,
                "money_type": 'coin'
            },
            {
                "amount": .5,
                "amount_2": 50,
                "money_type": 'cent'
            },
            {
                "amount": .2,
                "amount_2": 20,
                "money_type": 'cent'
            },
            {
                "amount": .1,
                "amount_2": 10,
                "money_type": 'cent'
            },
            {
                "amount": .05,
                "amount_2": 5,
                "money_type": 'cent'
            },
        ]

        cost_2 = ("{0:.2f}".format(self.cost))
        money_given_2 = ("{0:.2f}".format(self.money_given))
        change_2 = ("{0:.2f}".format(change))


        print(f"the cost of your purchase is: {cost_2} euro")
        print(f"You paid: {money_given_2} euro")
        print(f"The total change is: {change_2} euro\n")
        print(f"You will get back:\n")

        for m in money:
            amount = m["amount"]
            amount_2 = m["amount_2"]
            money_type = m["money_type"]
            if change / amount >= 1:
                amount_value = math.floor(change / amount)
                change = change%amount
                
                amount = ("{0:.2f}".format(amount))
                
                print(f"{amount_2} euro {money_type}: {amount_value}")


Person1 = ChangeReturn()