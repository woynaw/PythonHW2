print("Введите n")
n = int(input())
print("Введите m")
m = int(input())
print("Введите элементы первого массивa")
a = [int(input()) for item in range(n)]
print("Введите элементы второго массивa")
b = [int(input()) for item in range(m)]
c = a + b
c = set(c)
print(*c)