/*
 * @Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @Date: 2024-01-31 14:16:54
 * @LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @LastEditTime: 2024-01-31 14:17:07
 * @FilePath: /vscode_cpp_for_Mac-master/Palindrome_Number.c
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
bool isPalindrome(int x) {
    char text[20];
    sprintf(text, "%d", x);
    int len = strlen(text);
    char text_cmp[len + 1];
    text_cmp[len] = '\0';
    int j = 0;
    for (int i = len - 1; i >= 0; i--) {
        text_cmp[j] = text[i];
        j++;
    }

    if (strcmp(text, text_cmp) == 0) {
        return true;
    } else {
        return false;
    }
}