'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-14 16:57:41
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import heapq
def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    ugly_numbers = [1]  # 儲存醜數
    seen = {1}  # 避免重複
    heap = [1]  # 最小堆

    for _ in range(n):  # 迭代 n 次，找到第 n 個醜數
        smallest = heapq.heappop(heap)  # 取出最小的醜數

        for factor in [2, 3, 5]:  # 產生新的醜數
            new_ugly = smallest * factor
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)

    return smallest  # 第 n 個醜數

def main():
    print(nthUglyNumber(10))
    return 0

if __name__ == "__main__":
    main()