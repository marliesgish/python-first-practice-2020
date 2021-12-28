'''
Calculate the monthly payments of a fixed term mortgage over given Nth terms_number at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
'''

import math

class MortgageCalculator():

    def __init__(self, interest):
        self.amount_total = self.get_amount_total()
        self.interest = interest
        self.interest_usable = interest/100+1
        self.years_total = self.get_years_total()
        self.terms_year = self.get_terms_year()      
        self.terms_total_readable, self.terms_total_number = self.get_terms_total()
        self.terms_payment = self.get_terms_payment()
        self.terms_dict = self.get_terms_dict()
        self.terms_plural_singular = self.get_terms_plural_singular()
        self.years_plural_singular = self.get_years_plural_singular()
        self.get_printed_information()

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
            years_total = input("In how many years would you like to pay your mortgage back?")
            if years_total.isnumeric():
                return years_total
            else:
                print("Your input is not valid, please try again\n")
                continue


    def get_terms_year(self):
        terms_dict = {
            "yearly":1,
            "monthly":12,
            "weekly":52,
            "daily":365,
            }
        return terms_dict


    def get_terms_total(self):
        while True:
            terms_readable = input("How often would you like to have your payments: 'yearly', 'monthly', 'weekly' or 'daily'?")
            
            terms_total_readable = terms_readable.lower()
            
            for key, value in self.terms_year.items():
                if key == terms_readable:
                    terms_total_readable = key
                    terms_total_number = value
                    terms_total_number = int(terms_total_number)*int(self.years_total)
                    return terms_total_readable, terms_total_number
            else:
                print("Your input is not valid, please try again\n")
                continue


    def get_terms_payment (self):
        amount_total = float(self.amount_total)
        terms_total_number_1 = self.terms_total_number
        terms_total_number_2 = terms_total_number_1

        term_plusinterest = []

        while amount_total > 0 and terms_total_number_1 > 0:
            amount_total *= self.interest_usable
            terms_payment = amount_total / terms_total_number_2
            terms_year_number = (self.terms_year[self.terms_total_readable])

            while amount_total > 0 and terms_year_number > 0:
                term_plusinterest.append(terms_payment)
                amount_left = amount_total - terms_payment
                amount_total = amount_left
                terms_total_number_1 -=1
                terms_year_number -= 1

        terms_payment = (((sum(term_plusinterest))+amount_left)/terms_total_number_2)
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


    def get_terms_plural_singular(self):
        t = self.terms_dict[self.terms_total_readable]
        return t["plural"] if int(self.terms_total_number) > 1 else t["singular"]


    def get_years_plural_singular(self):
        y = self.terms_dict["yearly"]
        return y["plural"] if int(self.terms_total_number) > 1 else y["singular"]
        

    def get_printed_information(self):
        total_interest_euros = (float(self.terms_payment) * float(self.terms_total_number))-float(self.amount_total)
        total_interest_euros = "{:.2f}".format(math.ceil(total_interest_euros*20)/20) 


        print(f"Mortgage: € {self.amount_total}")
        print(f"Yearly interest: {self.interest}%")
        print(f"Total interest: €{total_interest_euros} ")
        print(f"{self.years_plural_singular.capitalize()}: {self.years_total}")
        print(f"Period: {self.terms_total_number} {self.terms_plural_singular}")
        print(f"\nYou will have to pay €{self.terms_payment} {self.terms_total_readable} for {self.terms_total_number} {self.terms_plural_singular}.")
        

person = MortgageCalculator(5.2)

