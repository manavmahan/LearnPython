def fib():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a