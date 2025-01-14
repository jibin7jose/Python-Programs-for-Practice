# Python Program to Sort Words in Alphabetic Order.

# a = "Jibin is Fire"
a = input("Enter Something Here: ")
b = a.split()

print(b)

for i in range (len(b)):
    b[i] = b[i].lower()


b.sort()


# for Alphabetic Order
for i in b:
    print(i)