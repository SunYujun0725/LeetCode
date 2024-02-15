
def main():
    n = 10
    x = 2.000000
    ans = 1
    if n > 0:
        tmp = x
        i = 1
        while n > 0:
            while 2**i < n:
                tmp *= tmp
                i += 1
            n -= 2**(i-1)
            i = 1
            ans *= tmp
            tmp = x
    elif n < 0:
        n = abs(n)
        x = 1.0/x
        tmp = x
        i = 1
        while n > 0:
            while 2**i < n:
                tmp *= tmp
                i += 1
            n -= 2**(i-1)
            i = 1
            ans *= tmp
            tmp = x
    else:
        ans = 1
    print(round(ans, 5))
    return round(ans, 5)

if __name__ == "__main__":
    main()