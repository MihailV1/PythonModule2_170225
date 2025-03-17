# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint

print("введите в диапазоне от -100 до 100")
while True:
    n = int(input("ввод: "))
    if -100 <= n <= 100:
        break

while n > 0:
    number = random.randint(-100, 100)
    numbers += [number]
    n -=1

print(numbers)
