
def main():
    letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    n = 701
    str_ans = ""
    if n <= 26:
        ans_len = 1
    else:
        ans_len = 1
        while 1:
            n -= 26**ans_len
            if (n > (26**(ans_len+1))):
                ans_len += 1
            else:
                break
        ans_len += 1
 
    for i in range(ans_len-1):
        if n%(26**(ans_len-i-1)) == 0:
            index = n//(26**(ans_len-i-1))
            str_ans = str_ans + str(letter[index-1])
            n = 0
        else:
            index = n//(26**(ans_len-i-1))
            str_ans = str_ans + str(letter[index])
            n = n%(26**(ans_len-i-1))

    str_ans = str_ans + str(letter[n-1])
    print(str_ans)

    return 0

if __name__ == "__main__":
    main()