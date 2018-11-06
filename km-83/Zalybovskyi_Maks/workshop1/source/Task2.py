def SumFunction(x,n):
    for n in range(0,n+1):
        sum += (x+n)/x**2
    return sum
x = int(input("Введіть х :"))
n = int(input("Введіть n: "))


print("Результат вашої операції :",SumFunction(x,n))