# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, -5]
k = 6
min = list_1[0]
min_delta = abs(k - min)
for i in list_1:
    delta = abs(k - i)
    if delta < min_delta:
       min_delta = delta
       min = i

print(min)












