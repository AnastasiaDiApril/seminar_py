# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list_1 = [0, -1, 5, 2, 3]
count = 0
for i in range(len(list_1)-1):
    if list_1[i] < list_1[i+1]:
        print(list_1[i], '<', list_1[i+1], end='\t')
        count +=1
print()
print(count)   