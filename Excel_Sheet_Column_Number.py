class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        ans = 0
        # 字母映射到數字
        letter_to_number = {char: str(ord(char) - ord('A') + 1) for char in letter}
        str_col = columnTitle
        str_index = 0
        for i in range(len(str_col)-1, -1, -1):
            ans += (int(letter_to_number[str_col[str_index]])*(26**i))
            str_index += 1
        
        #print(ans)
        return ans