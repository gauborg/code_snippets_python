'''
Description: The aim of this code is to identify if a given numer is a power of 2.
The program requires user input.
The method keeps bisecting the number by 2 until no further division by 2 is possible.

'''


def check_power_of_two(a, val):
    # first check if a is odd or equal to zero or an integer
    if (a <= 0):
        print("Number is zero!")
        return None
    elif (a%2 != 0):
        print("Odd number! Cannot be a power of 2!")
        return None
    else:
        residual = a
        count = 0
        while((residual != 0)):
            if (residual%2 == 1):
                return None
            # go on dividing by 2 every time
            half = residual/2
            residual -= half
            count += 1
            # stop when the final residual reaches 1
            if (residual == 1):
                break
        
        return count

# user input for number
number = int(input("Enter a number = "))

# call function to check if the number is power of 2.
power = check_power_of_two(number, 0)

if (power != None):
    print("The number is a power of 2, power =", power)
elif(power == None):
    print("The number is not a power of 2.")