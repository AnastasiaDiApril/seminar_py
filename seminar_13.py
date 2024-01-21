def reverse_nums(n):
    if n == 0:
        return ''
    k = int(input("Введите число последовательности: "))
    return f'{reverse_nums(n - 1)} {k}'


num = int(input('Введите количество чисел '))
print(reverse_nums(num))
