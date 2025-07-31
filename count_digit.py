number=int(input("Enter the number : "))
def count_digit(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
print("The number of digits in the number is:", count_digit(number))

    
    


