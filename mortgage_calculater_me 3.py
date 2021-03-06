'''
Calculate the monthly payments of a fixed term mortgage over given Nth terms_number at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
'''

import math


class MortgageCalculator():

    def __init__(self, interest):
        self.amount_total = self.get_amount_total()
        self.interest = interest
        self.start()

    def start(self):
        years_total = self.get_years_total()
        months_total = int(years_total) * 12
        terms_year = self.get_terms_year()
        terms_total_readable, terms_total_number = self.get_terms_total(
            years_total, terms_year)
        payment_per_term = self.get_payment_per_term(years_total,
                                                     months_total, terms_total_number)
        terms_dict = self.get_terms_dict()
        terms_plural_singular = self.get_terms_plural_singular(
            terms_total_readable, terms_total_number, terms_dict)
        years_plural_singular = self.get_years_plural_singular(
            terms_total_number, terms_dict)

        self.get_printed_information(years_total, terms_total_readable, terms_total_number, payment_per_term,
                                     terms_plural_singular, years_plural_singular)

    def get_amount_total(self):
        while True:
            amount_total = input("What is the amount of mortgage in euros?")
            if amount_total.isnumeric():
                return amount_total
            else:
                print("Your input is not valid, please try again\n")
                continue

    def get_years_total(self):
        while True:
            years_total = input(
                "In how many years would you like to pay your mortgage back?")
            if years_total.isnumeric():
                return years_total
            else:
                print("Your input is not valid, please try again\n")
                continue

    def get_terms_year(self):
        terms_dict = {
            "yearly": 1,
            "monthly": 12,
            "weekly": 52,
            "daily": 365,
        }
        return terms_dict

    def get_terms_total(self, years_total, terms_year):
        while True:
            terms_readable = input(
                "How often would you like to have your payments: 'yearly', 'monthly', 'weekly' or 'daily'?")

            terms_total_readable = terms_readable.lower()

            for key, value in terms_year.items():
                if key == terms_readable:
                    terms_total_readable = key
                    terms_total_number = value
                    terms_total_number = int(
                        terms_total_number)*int(years_total)
                    return terms_total_readable, terms_total_number
            else:
                print("Your input is not valid, please try again\n")
                continue

    def get_payment_per_term(self, years_total, months_total, terms_total_number):
        interest_usable = self.interest/100/12
        monthly_payment = interest_usable / \
            (1 - (1 + interest_usable)**(-int(months_total))) * \
            float(self.amount_total)
        print(monthly_payment)
        payment_per_term = (float(monthly_payment)*12) * int(years_total) / \
            int(terms_total_number)

        return float(payment_per_term)

    def get_terms_dict(self):
        terms_dict = {
            "yearly": {
                "singular": "year",
                "plural": "years"
            },
            "monthly": {
                "singular": "month",
                "plural": "months"
            },
            "weekly": {
                "singular": "week",
                "plural": "weeks"
            },
            "daily": {
                "singular": "day",
                "plural": "days"
            }
        }
        return terms_dict

    def get_terms_plural_singular(self, terms_total_readable, terms_total_number, terms_dict):
        t = terms_dict[terms_total_readable]
        return t["plural"] if int(terms_total_number) > 1 else t["singular"]

    def get_years_plural_singular(self, terms_total_number, terms_dict):
        y = terms_dict["yearly"]
        return y["plural"] if int(terms_total_number) > 1 else y["singular"]

    def get_printed_information(self, years_total, terms_total_readable, terms_total_number, payment_per_term,
                                terms_plural_singular, years_plural_singular):

        amount_total = "{:.2f}".format(
            math.ceil(float(self.amount_total)*20)/20)

        amount_total_interest = (
            float(payment_per_term) * int(terms_total_number)) - float(self.amount_total)
        amount_total_interest = "{:.2f}".format(
            math.ceil(float(amount_total_interest)*20)/20)

        payment_per_term = "{:.2f}".format(
            math.ceil(float(payment_per_term)*20)/20)

        print(f"Mortgage: ??? {amount_total}")
        print(f"Yearly interest: {self.interest}%")
        print(f"Total interest: ???{amount_total_interest} ")
        print(f"{years_plural_singular.capitalize()}: {years_total}")
        print(
            f"Period: {terms_total_number} {terms_plural_singular}")
        print(
            f"\nYou will have to pay ???{payment_per_term} {terms_total_readable} for {terms_total_number} {terms_plural_singular}.")


MortgageCalculator(5.2)
