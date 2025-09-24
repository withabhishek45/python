number = int(input("Enter a number to check divisible by 10 : "))
def zerodivisionerror(number):
    try:
        result = 10 / number
    except ZeroDivisionError :
        print("Error: Division by zero is not allowed.")
    else:
        print("The result is:", result)


zerodivisionerror(number)

