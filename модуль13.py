ticket = int(input("кол-во билетов:"))
age = int(input("возраст:"))
if age<18:
    ticket=ticket*0
elif 18<= age <=25:
    ticket=ticket*990
else:
    ticket=ticket*1390
print("сумма к оплате: ")
print(ticket)


