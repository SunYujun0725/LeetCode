

def main():
    s = " "
    Max = 0
    ans = 0
    word = ""
    i = 0
    d = 0
    while i < len(s):
        if s[i] not in word:
            ans += 1
            Max = max(Max, ans)
            word += str(s[i])
            i += 1
        else:
            i = d + word.index(s[i])
            s = s[:i] + '-' + s[i+1:]
            word = ""
            ans = 0
            i += 1
            d = i

    print(Max)
    return Max

if __name__ == "__main__":
    main()