'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-12 12:10:42
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def sumOfMultiples(n):
    """
    :type n: int
    :rtype: int
    """
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            sum += i
    return sum


def main():
    nums = 10
    print(sumOfMultiples(nums))
    return 0 

if __name__ == "__main__":
    main()