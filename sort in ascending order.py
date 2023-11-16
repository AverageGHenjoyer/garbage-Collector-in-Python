#(Sort in Ascending Order) Write a script that inputs three different
#floating-point numbers from the user. Display the numbers in increasing
#order. Recall that an if statement’s suite can contain more than one
#statement. Prove that your script works by running it on all six possible
#orderings of the numbers.
first_number = float(input("podaj pierwsza liczbe"))
second_number = float(input("podaj druga liczbe"))
third_number = float(input("podaj trzecia liczbe"))
if first_number < second_number and first_number < third_number and second_number < third_number:
    print(first_number, second_number, third_number)
if second_number < first_number and second_number < third_number and first_number < third_number:
    print(second_number, first_number, third_number)
if third_number < first_number and third_number < second_number and second_number < first_number:
    print(third_number, second_number, first_number)
if first_number < second_number and third_number < second_number:
    print(first_number, third_number, second_number)