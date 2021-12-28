'''
Calculate the monthly payments of a fixed term mortgage over given Nth terms_number at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
'''

import math


class MortgageCalculator():

    def __init__(self):
        self.amount_total = self.get_amount_total()
        self.interest = 5.2
        self.years_total = self.get_years_total()
        self.months_total = self.years_total*12
        self.monthly_payment = self.get_monthly_payment()
        self.get_printed_information()

    def get_amount_total(self):
        while True:
            amount_total = input("What is the amount of mortgage in euros?")
            if amount_total.isnumeric():
                return float(amount_total)
            else:
                print("Your input is not valid, please try again\n")
                continue

    def get_years_total(self):
        while True:
            years_total = input(
                "In how many years would you like to pay your mortgage back?")
            if years_total.isnumeric():
                return int(years_total)
            else:
                print("Your input is not valid, please try again\n")
                continue

    def get_monthly_payment(self):
        amount_total = self.amount_total
        interest = self.interest
        monthly_interest = interest / 100 / 12
        months_total = float(self.months_total)

        monthly_payment = monthly_interest / \
            (1 - (1 + monthly_interest)**(-months_total)) * amount_total
        return float(monthly_payment)

    def get_printed_information(self):
        amount_total = self.amount_total
        amount_total = "{:.2f}".format(math.ceil(amount_total*20)/20)

        amount_total_interest = (
            self.monthly_payment * float(self.months_total)) - self.amount_total
        amount_total_interest = "{:.2f}".format(
            math.ceil(amount_total_interest*20)/20)

        monthly_payment = self.monthly_payment
        monthly_payment = "{:.2f}".format(math.ceil(monthly_payment*20)/20)

        print(f"Mortgage: € {amount_total}")
        print(f"Yearly interest: {self.interest}%")
        print(f"Total interest: €{amount_total_interest} ")
        print(f"Years: {self.years_total}")
        print(f"Period: {self.months_total} months")
        print(
            f"\nYou will have to pay €{monthly_payment} for {self.months_total} months.")


person = MortgageCalculator()
