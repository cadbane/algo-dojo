def gcd(a, b):
    if a == b:
        return a

    # if a > b:
    #     return gcd(a-b, b)
    # else:
    #     return gcd(a, b-a)

    return (lambda: gcd(a-b, b), lambda: gcd(a, b-a))[a < b]()


if __name__ == '__main__':
    print(gcd(10, 100))
    print(gcd(24, 6))
    print(gcd(3, 10))