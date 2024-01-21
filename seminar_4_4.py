# задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

n = int(input("введите число "))
# max_number = 1000
# while n != 0:
#     n = int(input(""))
#     if max_number > n:
#         max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 
max_number = 0
while True:
    n = int(input("введите число "))
    if n == 0:
        break
    if n > max_number:
        max_number = n
    
print(max_number)