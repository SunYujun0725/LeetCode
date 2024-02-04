
def main():
    num1 = "1"
    num2 ="9"
    ans = ""
    cov_num1 = num1[::-1]
    cov_num2 = num2[::-1]
    carry_in = 0
    if len(cov_num1) >= len(cov_num2):
        for i in range(len(cov_num1)):
            if i < len(cov_num2):
                current_num = (int(cov_num1[i]) + int(cov_num2[i]) + carry_in)
                if current_num <= 9:
                    ans += str(current_num)
                    carry_in = 0
                else:
                    ans += str(current_num-10)
                    carry_in = 1
            else:
                current_num = (int(cov_num1[i]) + carry_in)
                if current_num <= 9:
                    ans += str(current_num)
                    carry_in = 0
                else:
                    ans += str(current_num-10)
                    carry_in = 1
        if carry_in == 1:
            ans += str(1)
    else:
        for i in range(len(cov_num2)):
            if i < len(cov_num1):
                current_num = (int(cov_num1[i]) + int(cov_num2[i]) + carry_in)
                if current_num <= 9:
                    ans += str(current_num)
                    carry_in = 0
                else:
                    ans += str(current_num-10)
                    carry_in = 1
            else:
                current_num = (int(cov_num2[i]) + carry_in)
                if current_num <= 9:
                    ans += str(current_num)
                    carry_in = 0
                else:
                    ans += str(current_num-10)
                    carry_in = 1
        if carry_in == 1:
            ans += str(1)
    print(ans[::-1])
    return 0



if __name__ == "__main__":
    main()