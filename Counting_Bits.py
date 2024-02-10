def main():
    n = 2
    ans = [0]
    l = 0
    for i in range(1, n+1):
        #將i轉成2進位
        count = 0
        while 2**l <= i:
            l += 1
        for j in range(l-1, -1, -1):
            if i >= 2**(j):
                i -= 2**(j)
                count += 1
        ans.append(count)
    print(ans)
    return 0


if __name__ == "__main__":
    main()