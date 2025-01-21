# Python Program to Convert Decimal to Binary Using Recursion.

def Convert_Binary(n):
    if n > 1:
        Convert_Binary(n//2)
    print(n%2, end= "")

print('The Binary of the Given Number is:')
Convert_Binary(27)