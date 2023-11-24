price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

price -= bonus if bonus_granted else print()


rating = 5
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')
# z piosenki De Mono - Niedziela będzie dla nas
today_weekday = "Friday"
print("Dzisiaj to ja pomagam mamie") if today_weekday == "Monday" else\
    print("Ty masz w domu pranie") if today_weekday == "Tuesday" or today_weekday == "Wednesday" else\
        print("Dzisiaj to ja mam dyżur") if today_weekday == "Thursday" else\
            print("Dzisiaj w piątek dwa zebrania") if today_weekday == "Friday" else\
            print("Dzisiaj sobota to znów nie możesz, bo na lekcję ganiasz") if today_weekday == "Saturday" else\
                print("Dzisiaj jest niedziela, niedziela będzie dla nas")