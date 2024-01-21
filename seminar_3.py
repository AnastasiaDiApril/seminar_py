# # Цикл для подсчета дней с ср.суточной температурой > 0
# n = int(input("Введите кол-во дней:"))
# i = 0
# count = 0
# max = 0
# while i < n:
#     temp = int(input("Введите теипературу:"))
#     if temp > 0:
#         count += 1
#         if count > max:
#             max = count
#     #elif count > max:
#         #max = count
#     else: 
#         count = 0
#     i += 1

# print(max)

n = int(input())

count = 0
maxx = 0

for i in range(n):
    temp = int(input())
    if temp > 0:
        if count > maxx:
            maxx = count
        count += 1
    else:
        count = 0
        
        
print(maxx)