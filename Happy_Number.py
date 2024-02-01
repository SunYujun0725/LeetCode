class Solution:
    def repeat_number(self, number_list, temp_number):
        for i in range(len(number_list)):
            if temp_number == number_list[i]:
                return True
        return False

    def isHappy(self, n: int) -> bool:
        number_list = []
        while 1:
            str_n = str(n)
            temp_number = 0 
            for i in range(len(str_n)):
                temp_number += int(str_n[i])**2

            if temp_number == 1:
                #print("True")
                return True
            else:
                #先判斷是否有出現過
                if self.repeat_number(number_list, temp_number) is True:
                    #print("False")
                    return False
                else:
                    number_list.append(temp_number)
        
            n = temp_number


