'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-01 19:48:33
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-09 00:43:26
FilePath: /vscode_cpp_for_Mac-master/Search_Insert_Position.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reverse_s = s[::-1]
        ans = 0
        for i in range(len(reverse_s)):
            if reverse_s[i].isalpha():
                ans += 1
                if i+1 == len(reverse_s):
                    return ans
                if reverse_s[i+1].isalpha()==False:
                    return ans
            else:
                ans = 0     