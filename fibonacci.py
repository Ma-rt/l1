def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


k = int(input("Введите число:"))
i = 1
result = 0
while k != result and k > result:
    result = fibonacci(i)
    i += 1

if k == result:
    print("Относится к фибоначчи")
else:
    print("Не относится к фибоначчи")
