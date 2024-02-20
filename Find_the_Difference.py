'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-20 00:36:01
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-20 22:45:39
FilePath: /vscode_cpp_for_Mac-master/Find_the_Difference.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(t)):
            if t[i] not in s:
                return t[i]
            else:
                index= s.index(t[i])
                s = s[:index] + '-' + s[index+1:]
