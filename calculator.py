import math as m

def add (x, y):
    return x + y

def sub (x, y):
    return x - y

def multiply(x, y):
	return x * y
	
def divison (x, y):
	return x / y

def log(x, y):
    log = m.log(x) + m.log(y)
    antilog = 10**log
    return antilog

	
while True:

    try:

        x = int(input("pls enter a no. "))

        y = int(input("pls enter a no. " ))

        break

    except ValueError:
        print("Invalid input")


print("pls select operation")

print("1.add")

print("2.sub")

print("3.multiply")

print("4.divison")

while True:

    choice = input("pls select operatio:  ")

    if choice in ('1','2','3','4','5'):


        if choice == '1':
            print(add(x , y))

        elif choice == '2':
            print(sub(x , y))
            
        elif choice =='3':
        	print(multiply(x , y))
        
        elif choice =='4':
        	print(divison(x , y))
        
        elif choice =='5':
            print(log(x , y))

        break

    else:

        print("invalid")