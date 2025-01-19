# Python Program to Count the Number of Each Vowel.

# Method 1 : Using Dictionary
# s = "My Name is Jibin Jose"
# vowels = "aeiou"

# s = s.casefold()
# print(s)

# count = {}.fromkeys(vowels,0)

# for char in s:
#     if char in count:
#         count[char]+=1

# print(count)

# Method 2 : Using List And Dictionary Comprehension
s = "My Name is Jibin jose"
vowels = "aeiou"

s = s.casefold()

count = {key:sum([1 for char in s if char == key]) for key in vowels}
print(count)