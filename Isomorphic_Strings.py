def main():
    s = "abb"
    t = "egg"
    change_chr = ""
    change_chr2 = ""
    change_chr3 = ""
    for i in range(len(s)):
        if s[i] not in change_chr3:
            if t[i] in change_chr2:
                return False
            change_chr += s[i] + t[i]
            change_chr2 += t[i]
            change_chr3 += s[i]
            s = s[:i] + t[i] + s[i+1:]
        else:
            index = 0
            for j in range(0, len(change_chr), 2):
                if change_chr[j] == s[i]:
                    index = j
            s = s[:i] + change_chr[index+1] + s[i+1:]
        print(s)
    if s == t:
        print(True)
        return True
    else:
        print(False)
        return False

if __name__ == "__main__":
    main()