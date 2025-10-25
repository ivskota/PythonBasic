number = int(input("Введіть число будь яке 5-значне число і я покажу його задом-наперед. Чекаю: "))

a, b = divmod(number, 10000)
c, d = divmod(b, 1000)
e, f = divmod(d, 100)
g, h = divmod(f, 10)

rev = h*10000 + g*1000 + e*100 + c*10 + a

print("Перевернуте число:", rev)


