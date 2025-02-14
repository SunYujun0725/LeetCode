'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-12 12:33:29
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def sortPeople(names, heights):
    """
    :type names: List[str]
    :type heights: List[int]
    :rtype: List[str]
    """
    
    # 將 names 和 heights 組合成一個 tuple list，然後依照 heights 進行排序（降序）
    sorted_people = sorted(zip(heights, names), reverse=True)
    
    # 提取排序後的 names
    return [name for _, name in sorted_people]

def main():
    print(sortPeople(["SUN", "Yu", "Chun"], [150, 170, 140])) # 2+5*3=13
    return 0 

if __name__ == "__main__":
    main()