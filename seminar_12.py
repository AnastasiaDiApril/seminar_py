def prime_num(num):
    
    for div in range(2,num):
        if num%div==0: 
            return False
    return True

        
num=int(input("Введите число: "))
print(prime_num(num))