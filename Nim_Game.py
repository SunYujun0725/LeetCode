'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-12 12:10:42
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    if (n % 4) == 0:
        return False
    else:
        return True

def main():
    nums = 10
    print(canWinNim(nums))
    return 0 

if __name__ == "__main__":
    main()