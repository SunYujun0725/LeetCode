
def main():
    haystack = "leetcode"
    needle = "leeto"
    cmp_len = len(needle)
    for i in range(len(haystack)-cmp_len+1):
        word = haystack[i:i+cmp_len]
        if word == needle:
            print(i)
            return i
    print(-1)
    return -1

if __name__ == "__main__":
    main()