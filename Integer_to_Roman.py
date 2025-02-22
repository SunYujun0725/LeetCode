'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-22 23:43:27
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

"""
I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
"""
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    # 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000
    # I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M
    roman = ''
    while num > 0:
        if num >= 1000:
            roman += 'M'
            num -= 1000
        elif num >= 900:
            roman += 'CM'
            num -= 900
        elif num >= 500:
            roman += 'D'
            num -= 500
        elif num >= 400:
            roman += 'CD'
            num -= 400
        elif num >= 100:
            roman += 'C'
            num -= 100
        elif num >= 90:
            roman += 'XC'
            num -= 90
        elif num >= 50:
            roman += 'L'
            num -= 50
        elif num >= 40:
            roman += 'XL'
            num -= 40
        elif num >= 10:
            roman += 'X'
            num -= 10
        elif num >= 9:
            roman += 'IX'
            num -= 9
        elif num >= 5:
            roman += 'V'
            num -= 5
        elif num >= 4:
            roman += 'IV'
            num -= 4
        elif num >= 1:
            roman += 'I'
            num -= 1
    return roman


def main():
    print(intToRoman(3749))
    return 0

if __name__ == "__main__":
    main()