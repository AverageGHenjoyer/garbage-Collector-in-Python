first = int(input("first number"))
second = int(input("second number"))
third = int(input("third number"))

min = first

if min > second:
    min = second
if min > third:
    min = third
print(f"The smallest of these three is: {min}")