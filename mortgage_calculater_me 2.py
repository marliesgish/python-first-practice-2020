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
        interest_usable = self.interest/100+1
        years_total = self.get_years_total()
        terms_year = self.get_terms_year()
        terms_total_readable, terms_total_number = self.get_terms_total(
            years_total, terms_year)
        terms_payment = self.get_terms_payment(
            interest_usable, terms_year, terms_total_readable, terms_total_number)
        terms_dict = self.get_terms_dict()
        terms_plural_singular = self.get_terms_plural_singular(
            terms_total_readable, terms_total_number, terms_dict)
        years_plural_singular = self.get_years_plural_singular(
            terms_total_number, terms_dict)

        self.get_printed_information(years_total, terms_total_readable, terms_total_number, terms_payment,
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

    def get_terms_payment(self, interest_usable, terms_year, terms_total_readable, terms_total_number):
        amount_total = float(self.amount_total)
        terms_total_number_1 = terms_total_number
        terms_total_number_2 = terms_total_number_1

        term_plusinterest = []

        while amount_total > 0 and terms_total_number_1 > 0:
            amount_total *= interest_usable
            terms_payment = amount_total / terms_total_number_2
            terms_year_number = (terms_year[terms_total_readable])

            while amount_total > 0 and terms_year_number > 0:
                term_plusinterest.append(terms_payment)
                amount_left = amount_total - terms_payment
                amount_total = amount_left
                terms_total_number_1 -= 1
                terms_year_number -= 1

        terms_payment = (
            ((sum(term_plusinterest))+amount_left)/terms_total_number_2)
        terms_payment = "{:.2f}".format(math.ceil(terms_payment*20)/20)
        return terms_payment

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

    def get_printed_information(self, years_total, terms_total_readable, terms_total_number, terms_payment,
                                terms_plural_singular, years_plural_singular):
        total_interest_euros = (float(
            terms_payment) * float(terms_total_number))-float(self.amount_total)
        total_interest_euros = "{:.2f}".format(
            math.ceil(total_interest_euros*20)/20)

        print(f"Mortgage: € {self.amount_total}")
        print(f"Yearly interest: {self.interest}%")
        print(f"Total interest: €{total_interest_euros} ")
        print(f"{years_plural_singular.capitalize()}: {years_total}")
        print(
            f"Period: {terms_total_number} {terms_plural_singular}")
        print(
            f"\nYou will have to pay €{terms_payment} {terms_total_readable} for {terms_total_number} {terms_plural_singular}.")


person = MortgageCalculator(5.2)
