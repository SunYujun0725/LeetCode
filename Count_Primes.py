'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-14 16:45:11
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import math
def countPrimes(n):
    """
    使用埃拉托色尼篩法計算小於 n 的質數個數
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0  # 沒有小於 2 的質數

    # 建立布林陣列，預設所有數字都是質數
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是質數

    # 遍歷 2 到 sqrt(n)，篩選掉所有合數
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:  # 如果 i 是質數
            # 標記 i 的倍數為 False（從 i*i 開始）
            for j in range(i * i, n, i):
                is_prime[j] = False

    # 計算布林陣列中 True 的個數，即為質數數量
    return sum(is_prime)

def main():
    print(countPrimes(10))
    return 0

if __name__ == "__main__":
    main()