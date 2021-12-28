'''
Have the user enter a number and find all Prime Factors 
(if there are any) and display them.
'''

def get_primes(max_range):
    primes = [2]
    
    numbers = list(range(3, max_range+1, 2))
    for n in numbers:
        is_prime(n)
        if is_prime(n):
            primes.append(n)
    return primes


def is_prime(n):
    for y in range(3,n,2):  # test all odd factors up to x-1
        if n%y == 0:

            return False
    else:
        return True


def print_primes(primes):
    print(f'The amount of prime numbers in the range of 0-{max_range} is {len(primes)}.\n')
    print(f'The prime number(s) in this range:')
    for prime in primes:
        print(prime)


while True:
    max_range = (input("Provide a number and see all the prime numbers up to this number.\n"))

    if max_range.isnumeric():
        if int(max_range) < 2:
            print('There are 0 prime numbers in this range of numbers.')
        else:
            result = get_primes(int(max_range))
            print_primes(result)
        break
    else:
        print("This is not a number.")
        continue