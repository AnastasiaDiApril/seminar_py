# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

n = int(input())
 
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
 
print(factorial)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# ёто есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

n0 = 0 # n-2 элемент
n1 = 1 # n-1 элемент
n = 1 # n = (n-2)+(n-1)
count = 1
res = 0
while (res<n):
    res = n0+n1
    n0 = n1
    n1 = res
    count += 1
#print(res)
if res==n:
    print(count)
else:
    print(-1)