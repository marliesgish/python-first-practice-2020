'''
Calculate the total cost of tile it would take to 
cover a floor plan of width and height, using a cost 
entered by the user.
'''

def input_cost():
    while True:
        cost_square_meter = input("Enter the amount of euros per m2 ")
        if cost_square_meter.isnumeric():
            cost_square_meter = int(cost_square_meter)
            break
        else:
            print("This is not a valid input")
            continue

    return cost_square_meter

def input_square_meter():
    while True:
        x = input("Enter the length of the surface in m2")
        if x.isnumeric():
            x = int(x)
            break
        else:
            print("This is not a valid input")
            continue
    
    while True:
        y = input("Enter the width of the surface in m2")
        if y.isnumeric():
            y = int(y)
            break
        else:
            print("This is not a valid input")
            continue

    squares = x*y
    return squares

def run_program():
    total_cost = (input_square_meter()) * (input_cost())
    print(f"The total cost will be {total_cost} euros")

run_program()