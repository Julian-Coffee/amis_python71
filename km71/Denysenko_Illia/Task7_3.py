print("\n Умова: Нехай число N - кількість хвилин, відрахованих після півночі. "
          "\n Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?"
          "\n Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). "
          "\n Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим."
          "\n Вхідні дані: 1 ціле число, що вводить користувач."
          "\n Вихідні дані: вивести два числа. Перше - години, друге - хвилини.\n")

time = float(input('Введіть кількість хвилин: '))

if (a>1440):
   b = a%1440
else:
   b = a
hourse = int(b//60)
minut = int(b%60)

print(x,':',y)