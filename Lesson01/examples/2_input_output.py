# =================================
#     Консольный ввод/вывод
# =================================

# print() - для вывода информации в консоль

name = 'Иван'
print('Приветствую,', name)

# input() - запросить ввод с клавиатуры
name = input('Введите ваше имя: ')
print('Приятно познакомиться,', name)

# функция input() всегда возвращает строку
# Если нужно, преобразуйте к числу (приведение типов)
n1 = int(input("n1: "))
n2 = int(input("n2: "))
print('сложение чисел n1 + n2 =', n1 + n2)
