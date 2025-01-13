# Python Program to Access Index of a List Using For Loop.

# Solution 1 : Using Enumerate Method
list = [7,17,27,37,47]
for index, value in enumerate(list, start=1):
    print(index,'-',value)

# Solution 2 : Not Using Enumerate Method
list = [7,17,27,37,47]
for index in range(len(list)):
    value = list[index]
    print(index,value)
    