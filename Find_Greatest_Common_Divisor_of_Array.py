'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-14 20:30:32
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def findGCD(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    sort_list = sorted(nums)
    smallest = sort_list[0]
    largest = sort_list[len(sort_list)-1]
    for i in range(1, largest+1):
        if (smallest % i == 0) and (largest % i == 0) :
            ans = i
    
    return ans

def main():
    print(findGCD([2, 10, 4, 5, 9, 3]))
    return 0

if __name__ == "__main__":
    main()