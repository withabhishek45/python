nums = list(map(int, input("Enter numbers separated by space: ").split()))

even_nums = [x for x in nums if x % 2 == 0]

print("Even numbers:", even_nums)
