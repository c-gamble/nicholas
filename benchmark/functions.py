#define a function to print calculate the remainder of an integer when it is divided by 10
def remainder(n):
    return n % 10
#ask the user to input an integer
num = int(input("Enter any integer:\n"))
#call the function and print its output
print(f'Remainder: {remainder(num)}')