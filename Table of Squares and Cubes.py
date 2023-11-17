number = 0
square = 2
cube = 3
print("number\tsquare\troot")
for x in range(0,6):
    number = x
    print(f"{number:>6}\t{number**square:>6}\t{number**cube:>4}")
