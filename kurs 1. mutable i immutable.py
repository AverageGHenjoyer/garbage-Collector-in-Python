days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
workdays = days.copy()
workdays.remove("sat")
workdays.remove("sun")
print(workdays)