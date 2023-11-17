
total = 0
grade = 0
grade_counter = 0
average = 0
the_sentinel = -1

while grade != the_sentinel:

    grade = int(input("Please provide here your grade or type -1 to quit: "))
    if grade == -1:
        print("Okay, quitting...")
    else:
        if grade > 101 or grade < 0:
            print('Wrong! You must provide an integer between 1 and 100. Please try again.')
        elif isinstance(grade, int) is True and 100 >= grade >= 0:
            total += grade
            grade_counter += 1

if grade_counter != 0:
    average = total / grade_counter
    print(f'Your average score is: {average}')
else:
    print('No grades were entered. ')
