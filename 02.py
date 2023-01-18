# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint
 
min = int(input('Введите минимум заданного диапозона: '))
max = int(input('Введите максимум заданного диапозона: '))

data = [randint(1, 15) for _ in range(15)]
print('Исходный массив:', data, sep='\n')

index = [i for i, v in enumerate(data) if min <= v <= max]
print('Индексы элементов:', index, sep='\n')

result = []
i = len(index)
while i :
    i -= 1
    result.append(data.pop(index[i]))
print('Элементы:', result, sep='\n')

