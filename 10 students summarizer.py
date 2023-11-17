"""A college offers a course that prepares students for the state licensing
exam for real-estate brokers. Last year, several of the students who
completed this course took the licensing examination. The college wants
to know how well its students did on the exam. You have been asked to
write a program to summarize the results. You have been given a list of
these 10 students. Next to each name is written a 1 if the student passed
the exam and a 2 if the student failed."""
passes = 0
failures = 0
user_input = None
total = 0
while total != 10:
    try:
        user_input = int(input('Provide the score: 1 for passed and 2 for failed. '))
    except:
        pass
    if user_input == 1:
        passes += 1
        total += 1
    elif user_input == 2:
        failures += 1
        total += 1
    else:
        print("Wrong answer! You need to provide 1 or 2.")
print(f"Passed: {passes}\n"
      f"Failed: {failures}")
if passes >= 8:
    print("Bonus for the instructor!")
