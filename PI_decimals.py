import math

'''
Enter a number and have the program generate π (pi) 
up to that many decimal places. Keep a limit to how 
far the program will go.
'''

pi = math.pi 

def pi_digit(n):
    pi_round = round(pi,n)
    print(pi_round)