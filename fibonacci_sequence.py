'''
Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number
'''

def input_fibonacci():
    while True:
        try:
            n = input ("Input a number and the Fibonacci sequence of that number (press 'q' to quit)")
            if n == 'q':
                break
            else:
                n = int(n)
                if n < 0:
                    print("Number must be bigger than 0")
            
        except ValueError:
            print("Input must be a number")
            continue
        
        else:
            return n     


def fibonacci(n): 
    if n==1: 
        return 0
# Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 
  

# Driver Program 
n = input_fibonacci()
fibonacci(n)