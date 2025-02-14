'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-14 15:42:21
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)  # 確保 k 不會超過陣列長度
    # 重新排列 nums（用切片賦值來修改原始列表）
    nums[:] = nums[-k:] + nums[:-k]

def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)
    return 0 

if __name__ == "__main__":
    main()