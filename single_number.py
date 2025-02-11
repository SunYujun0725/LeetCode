def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 由小到大排序
    sorted_nums = sorted(nums)  
    count = 0
    now_number = -40000
    for i in range(len(sorted_nums)):
        if now_number != sorted_nums[i] and count == 0:
            count += 1
            now_number = sorted_nums[i]
            if i == len(sorted_nums) - 1:
                return now_number
        elif now_number != sorted_nums[i] and count == 1:
            return now_number
        # 如果跟之前的一樣
        else:
            count = 0 
            now_number = sorted_nums[i]
 
# 1, 1, 2, 2, 4
def main():
    nums = [1]
    print(singleNumber(nums))
    return 0 

if __name__ == "__main__":
    main()