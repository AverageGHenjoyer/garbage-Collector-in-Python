number = int(input("Podaj liczbe prosze: "))
jeden = number // 10000
dwa = number // 1000 % 10
trzy = number // 100 % 10
cztery = number // 10 % 10
piec = number % 10

print (f"{jeden}   {dwa}   {trzy}   {cztery}   {piec}")