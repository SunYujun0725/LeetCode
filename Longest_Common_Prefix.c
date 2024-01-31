/*
 * @Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @Date: 2024-01-31 14:20:48
 * @LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @LastEditTime: 2024-01-31 14:21:01
 * @FilePath: /vscode_cpp_for_Mac-master/Longest_Common_Prefix.c
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
char *longestCommonPrefix(char **strs, int strsSize) {
    if (strsSize <= 1) {
        char *ans = strs[0];
        return ans;
    } else {
        int longestlen = strlen(strs[0]);
        for (int i = 0; i < strsSize; i++) {
            int tmplen = strlen(strs[i]);
            if (tmplen > longestlen) {
                longestlen = tmplen;
            }
        }
        int again = 0;
        int k = 0;
        char answer[longestlen + 1];
        for (int i = 0; i < longestlen + 1; i++) {
            answer[i] = '\0';
        }
        for (int i = 0; i < longestlen; i++) {
            for (int j = 0; j < strsSize - 1; j++) {
                if (strs[j][i] == strs[j + 1][i]) {
                } else {
                    again = 1;
                    break;
                }
            }
            if (again == 1) {
                answer[k] = '\0';
                break;
            } else {
                answer[k] = strs[0][i];
                k++;
            }
        }

        if (longestlen == 0) {
            char *ans = "";
            return ans;
        } else {
            char *ans = answer;
            return ans;
        }
    }
}