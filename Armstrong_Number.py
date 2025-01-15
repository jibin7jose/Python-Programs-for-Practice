#python program to check Armstrong Number

num = int(input("Enter the Number :"))
order = len(str(num))
sum = 0
temp = num


while temp > 0:
    digit = temp % 10
    cube = digit ** order
    sum = sum + cube
    temp = temp //10


if sum == num:
    print("Number is an Armstrong Number.")
else:
    print("Not an Armstrong Number.")


# Enter the Number :153
# Number is an Armstrong Number.
# Enter the Number :154
# Not an Armstrong Number.