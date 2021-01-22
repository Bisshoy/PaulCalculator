#Hi Paul! Here's my calculator. It's not pretty. 

#Here are all the operations. It's a simple calculator. So what.
#Sue me. 
def multiply (x, y):
    return x*y
def divide (x, y):
    return x/y
def add (x, y):
    return x+y
def subtract (x, y):
    return x-y

#First, we'll ask what operation you want to do. I say we, but it's
#just me, really. The royal we, I guess?
print("What operation would you like to do?: ")
print("1. Multiply / 2. Divide / 3. Add / 4. Subtract\n")

while True:
    operation = input("What operation? 1 / 2 / 3 / 4: ")
    
    if operation in ("1", "2", "3", "4"):
        a = float(input("First number: "))
        b = float(input("Second number: "))
        
        if operation == "1":
            print("The answer is: ", multiply(a, b))
        elif operation == "2":
            print("The answer is: ", divide(a, b))
        elif operation == "3":
            print("The answer is: ", add(a, b))
        elif operation == "4":
            print("The answer is: ", subtract(a, b))
        break
    else:
        print("I think you messed up somewhere, Paul.")
input("Press any key to exit.")
