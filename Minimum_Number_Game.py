'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-20 00:36:01
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-20 00:36:19
FilePath: /vscode_cpp_for_Mac-master/Minimum_Number_Game.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        cycle = len(nums)//2
        for i in range(cycle):
            first_min = min(nums)
            nums.remove(first_min)
            second_min = min(nums)
            nums.remove(second_min)
            arr.append(second_min)
            arr.append(first_min)
        return arr
