def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input('Введите какое число Фибоначчи отобразить: '))
print(n, '-ое по счёту число Фибоначчи это:', fib(n))
