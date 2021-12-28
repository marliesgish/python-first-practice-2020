import math

'''
Enter a number and have the program generate π (pi) 
up to that many decimal places. Keep a limit to how 
far the program will go.
'''

e = math.e

def e_digit(n):
    e_round = round(e,n)
    print(e_round)