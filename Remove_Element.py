'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-01 19:48:33
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-08 20:42:34
FilePath: /vscode_cpp_for_Mac-master/Remove_Duplicates_from_Sorted_Array.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = []
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
                new_nums.append(nums[i])
        nums.clear()
        for i in range(len(new_nums)):
            nums.append(new_nums[i])
            
        return count
        