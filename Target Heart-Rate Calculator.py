user_age = int(input("podaj swoj wiek ")) 
max_heart_rate = 220 - user_age
min_range = max_heart_rate // 2 
max_range = max_heart_rate * 0.85
print("Your maximum heart rate is ", max_heart_rate)
print(f"Your range of the optimum heart rate is between {min_range} and {max_range}") 