# Python Program to Delete An Element From a Dictionary.

# Method 1: Using Delete Statement
marks = {"Jibin":97,"Sigin":95,"Simi":99,"Alan":93}
print(marks)
del marks["Simi"]
print(marks)


# Method 2: Using pop() Function
marks = {"Jibim":97,"Sigin":95,"Kuttu":99,"Ajith":93}
pop_item = marks.pop("Kuttu ")
print(marks)
