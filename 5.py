def negaFib(n):

    if n == 0 or n == 1:
        return n
    if n == -1:
        return -n
    if n < 0:
        return round(negaFib(abs(n)) * (-1)**(n + 1))
    else:
        return negaFib(n - 1) + negaFib(n - 2)


n = int(input('Введите сколько элементов из негафиббоначчи вывести: '))
for i in range(-n, n + 1):
    print(negaFib(i), end=' ')