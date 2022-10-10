def fibonacci(n):
    a, b = 0,1
    c = a + b
    for i in range(n):
        yield a
        a,b = b, a+b

lista = fibonacci(10)


for i in lista:
    print(i)