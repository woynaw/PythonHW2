print("Введите N")
n = int(input())
print("Введите кол-во ягод на кустах")
kust = [int(input()) for item in range(n)]
max = 0
kust = kust + kust[:1]
for i in range(n):
    if (kust[i] + kust[i + 1] + kust[i - 1]) > max:
        max = kust[i] + kust[i + 1] + kust[i - 1]
print(max)
