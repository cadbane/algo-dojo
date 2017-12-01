def fib_sequence(n):
    # if n < 2:
    #     return n
    #
    # return fib_sequence(n-1) + fib_sequence(n-2)
    return n if n < 2 else fib_sequence(n-1) + fib_sequence(n-2)

if __name__ == '__main__':
    print(fib_sequence(-10))
    print(fib_sequence(19))