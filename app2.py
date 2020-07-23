from datetime import date, timedelta

current_date = date.today()
current_year = date.today().year
current_day = date.today().day - 1
month_before = date.today().month - 1


print(str(current_year))

print(current_date - timedelta(days=6))
print(current_date - timedelta(days=5))
print(current_date - timedelta(days=4))
print(current_date - timedelta(days=3))
print(current_date - timedelta(days=2))
print(current_date - timedelta(days=1))
print(current_date)

fechas = [1, 2, 3, 4, 5, 6, 7]
for i in range(7):
    fechas[i] = str(current_date - timedelta(days=i))
fechas.reverse()
print("--------")
for x in fechas:
    print(x)
