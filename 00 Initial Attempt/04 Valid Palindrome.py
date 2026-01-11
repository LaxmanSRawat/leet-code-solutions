class Solution(object):
    def isPalindrome(self, s):
        if len(s) <2:
            return True
        # s1 = ""
        # s2 = ""

        left_pointer = 0
        right_pointer = len(s)-1

        while(left_pointer < right_pointer):
            print(left_pointer,right_pointer, s[left_pointer], s[right_pointer])
            if(isalphanumeric(s[left_pointer]) and isalphanumeric(s[right_pointer])):
                if s[left_pointer].lower() != s[right_pointer].lower():
                    return False
                # s1=s1+s[left_pointer].lower()
                left_pointer = left_pointer + 1
                # s2=s2+s[right_pointer].lower()
                right_pointer = right_pointer -1
                continue
            elif(isalphanumeric(s[left_pointer])):
                right_pointer = right_pointer-1
            else:
                left_pointer=left_pointer+1
        
        # print(s1,s2,left_pointer,right_pointer)
        # if s1 == s2 or len(s1) + len(s2) == 1:
        #     return True
        
        return True

def isalphanumeric(val):
    return (val >= "A"  and val <= "Z") or (val >= "a"  and val <= "z") or (val >= "0"  and val <= "9") 
    
solution_obj = Solution()
print(solution_obj.isPalindrome("A man, a plan, a canal: Panama"))