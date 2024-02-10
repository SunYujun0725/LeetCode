class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp_list = s[::-1]
        s.clear()
        for i in range(len(tmp_list)):
            s.append(tmp_list[i])