'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-01 19:48:33
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-04 13:37:46
FilePath: /vscode_cpp_for_Mac-master/Power_of_Three.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while (3**i <= n):
            if (3**i == n):
                return True
            i += 1
        return False
            