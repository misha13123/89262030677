m = int(input(""))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = per_cent.copy()
maxval = list(per_cent.values())[0]
for key,value in per_cent.items():
    if value > maxval:
        maxval = value
    deposit[key] = value * m /100
print(deposit)
print("Максимальное значение ")
print(maxval*m/100)


