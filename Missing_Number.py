def main():
    nums = [9,6,4,2,3,5,7,0,1]
    number_list = [0] * (len(nums)+1)

    for i in range(len(nums)):
        number_list[nums[i]] = 1

    for i in range(len(number_list)):
        if number_list[i] == 0:
            print(i)
            return i

if __name__ == "__main__":
    main()