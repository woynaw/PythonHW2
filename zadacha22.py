print("Введите n")
n = int(input())
print("Введите m")
m = int(input())
print("Введите элементы первого массивa")
a = []
b = []
for i in range(n):
    a.append(int(input()))
print("Введите элементы второго массивa")
for i in range(m):
    b.append(int(input()))
c = a + b
c = set(c)
print(*c)