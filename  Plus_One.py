'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-01 19:48:33
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-01 20:51:41
FilePath: /vscode_cpp_for_Mac-master/Add_Binary.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""
        list_plus_one = []
        i = 0
        while (i < len(digits)):
            str_digits = str_digits + str(digits[i])
            i += 1
        int_digits = int(str_digits) + 1
        str_digits = str(int_digits)
        i = 0
        while (i < len(str_digits)):
            list_plus_one.append(int(str_digits[i]))
            i += 1
            
        return list_plus_one