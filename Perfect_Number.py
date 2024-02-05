
def main():
    num = 28
    divisor_sum = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            #factors.append(i)
            if i != num:
                divisor_sum += i
            if i != num // i:  # 避免重复添加平方因数
                #factors.append(n // i)
                if num//i != num:
                    divisor_sum += num//i
        i += 1
    
    if divisor_sum == num:
        print(True)
    else:
        print(False)
    return 0


if __name__ == "__main__":
    main()

