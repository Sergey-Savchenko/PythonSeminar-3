# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

from random import randint
numb = int(input('Введите количество элементов массива: '))
check = int(input('Введите проверочное число: '))
massiv = [randint(1,numb) for i in range (numb)]
print(massiv)
prov = numb
answer = numb
for i in range(numb):
    if abs(check - massiv[i])<prov:
        prov = abs(check - massiv[i])
        answer = massiv[i]
    if abs(check - massiv[i])==prov and massiv[i]<answer:
        answer = massiv[i]
    # print(prov)
print(f"Ближайший элемент массива: {answer}")