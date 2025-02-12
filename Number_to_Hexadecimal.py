'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-12 11:52:29
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def toHex(nums):
    """
    :type num: int
    :rtype: str
    """
    if nums == 0:
        return '0'
    hexs = '0123456789abcdef'
    res = ''
    while nums and len(res) < 8:
        res = hexs[nums & 0xf] + res
        nums >>= 4
    return res


def main():
    nums = 26
    print(toHex(nums))
    return 0 

if __name__ == "__main__":
    main()