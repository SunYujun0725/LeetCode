'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-01 19:48:33
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-05 22:32:10
FilePath: /vscode_cpp_for_Mac-master/Construct_the_Rectangle.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        min = 100000000000
        ans = []
        for i in range(1, area+1):
            if area%i == 0:
                if abs(i-(area/i)) <= min:
                    L = i
                    W = int(area/i)
                    if W > L:
                        #swap
                        temp = L
                        L = W
                        W = temp
                    min = L - W
        ans.append(L)
        ans.append(W)
        return ans