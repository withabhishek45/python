def check_non_numeric(value):
    if not value.isnumeric():   
        raise ValueError("Error: Non-numeric value passed!")
    else:
        print("Valid number:", int(value))

value = input("Enter a number: ")
check_non_numeric(value)
