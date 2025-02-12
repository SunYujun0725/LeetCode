'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-12 12:10:42
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    """
    分析基本情況
        如果有 1、2、3 顆石頭，你可以直接拿光, 獲勝
        如果有 4 顆石頭, 無論你拿幾顆(1、2、3), 對方都能拿走剩下的, 導致你輸掉遊戲
    找規律
        n = 5, 6, 7, 你可以讓對方進入 n = 4 的狀態(拿 1、2、3 顆),所以你必勝
        n = 8, 無論怎麼拿, 都會讓對方進入 n = 5, 6, 7 的狀態, 對方可以必勝
    結論：
        只要 n % 4 == 0, 你一定輸, 因為無論怎麼拿, 對方都可以讓你回到 n % 4 == 0 的情況
        否則，你一定贏
    """
    if (n % 4) == 0:
        return False
    else:
        return True

def main():
    nums = 10
    print(canWinNim(nums))
    return 0 

if __name__ == "__main__":
    main()