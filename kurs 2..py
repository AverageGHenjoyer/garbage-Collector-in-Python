def DisplayOptions(options):
    for i in range(len(options)):
        print(f"{i+1} - {options[i]}")
    choice = input("Select Option above or press enter to exit:")
    return choice


options = ['load data', 'export data', 'analyze & predict']
choice = 'x'


while choice:
    choice = DisplayOptions(options)

    if choice:
        try:
            choice_num = int(choice)
            if 0 < choice_num <= len(options):
                print(f"You selected: {choice_num} - {options[choice_num]}")
            else:
                print("Unfortunately your answer wasn't appropriate.")
        except:
            print("Unfortunately your answer wasn't appropriate."
                  "Your answer must be an integer.")
    else:
        print("Bad answer. Quitting...")
        break
