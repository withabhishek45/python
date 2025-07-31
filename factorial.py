n=int(input("Enter a number : "))

def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
    
print("the factorial of ",factorial(n))
