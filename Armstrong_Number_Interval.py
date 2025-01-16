# Python Program to find Armstrong Number in an Interval.
lower = int(input("Enter the Lower Limit Here: "))
upper = int(input("Enter the Upper Limit Here: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
        
