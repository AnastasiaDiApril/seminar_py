# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

# a = [1, 1, 2, 0, -1, 3, 4, 4]
# # a = map(int, input().split())
# # a = list(a)
# d = {}
# for i in a:
#     d[i] = 1
# print(len(d))

# numbers = [ 2, 2, 1]
# count = 0
# min = numbers[0]
# numbers1=[]

# for i in numbers:
#     if i not in numbers1:
#         numbers1.append(i)
# print(len(numbers1))

#второе решение
numbers = [2, 2, 1]

print(len(set(numbers)))
print(set(numbers))