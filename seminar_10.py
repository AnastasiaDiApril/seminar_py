from random import randint
n = int(input('Введите количество оценок: '))
list_1 = [randint(1, 5) for _ in range(n)]
print(list_1)

max_bal = max(list_1)
min_bal = min(list_1)
for i in range(len(list_1)):
    if list_1[i] == max_bal:
        list_1[i] = min_bal

print(list_1)

start_3 = time.time()

max_point = list_1[0]
min_point = list_1[0]
list_max_points = [0]

for i in range(len(list_1)):
    if list_1[i] > max_point:
        max_point = list_1[i]
        list_max_points = [i]
    elif list_1[i] == max_point:
        list_max_points.append(i)
    if list_1[i] < min_point:
        min_point = list_1[i]

for i in list_max_points:
    list_1[i] = min_point

end_3 = time.time()
# print(list_1)
print(f'{end_3 - start_3}')



