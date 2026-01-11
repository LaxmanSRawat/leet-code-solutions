class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            big_str = a
            sml_str = b
        else:
            big_str = b
            sml_str = a
        
        len_dif = len(big_str) - len(sml_str)
        
        sml_str = "0"*len_dif + sml_str
        carry = 0
        print(sml_str,big_str)
        result = ""
        for i in range(len(big_str)-1, -1,-1):
            print(big_str[i],sml_str[i],i)
            if big_str[i] == "1" and sml_str[i] == "1":
                if carry:
                    result = "1" + result
                else:
                    print("here a",i)
                    result = "0" + result
                    carry =1
            elif big_str[i] == "1" or sml_str[i] == "1":
                if carry:
                    result = "0" + result
                else:
                    result = "1" + result
            else:
                if carry:
                    result = "1" + result
                    carry = 0
                else:
                    result = "0" + result
        if carry:
            return "1" + result
        return result
        

print(Solution().addBinary("1010","1011"))