"""
Check Primality Functions
Exercise 11
Ask the user for a number and determine whether the number is prime or 
not. """

from sys import exit

def prime():
    number = input(
    "\nEnter a number to check if it is Prime number.\n"
    )

    if not number:
        exit(0)

    try: 
        number = int(number)
    except ValueError:
        print('invalid entry')
        exit(0)
    

    if number == 1 or number == -1 or number == 0:
        print("{} is not a Prime!".format(number))
        exit()
    elif number < 0 :        
        n = number * -1 
    else:
        n = number

    # d is for division or factor 
    # r is for remainder 
    # n is for number 

    d = n // 2 

    while d != 1:
        r = n % d 
        if r == 0:
            print("{} is not a Prime!".format(number))
            exit(0) 
            break 
        else:
            d -= 1 

    print("{} is a Prime!".format(number)) 

if __name__ == "__main__":
    prime()
