print("Введите количество билетов, которое хотите приобрести на мероприятие. При покупке от 4-х билетов действует скидка 10% от стоимости заказа!")
tickets = int(input())
price = 0
for i in range(tickets):
    age = int(input("Введите возраст"))
    if 18 <= age <= 25:
        price += 990
    elif age >= 25:
        price += 1390
if tickets >= 4:
    print("Сумма к оплате с учетом скидки: ", price - ((price / 100) * 10), "рублей")
else:
    print("Сумма к оплате: ", price, "рублей")       