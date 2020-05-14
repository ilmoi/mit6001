def fib_gen():
    fib_1 = 1
    fib_0 = 0
    while True:
        next = fib_1+fib_0
        print(next)
        yield next
        
        fib_0 = fib_1
        fib_1 = next
        
fib = fib_gen()
fib.__next__()
fib.__next__()
fib.__next__()
fib.__next__()