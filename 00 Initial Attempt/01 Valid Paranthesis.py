class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        history_array = []
        # print('s=',s)

        for i in range(0, len(s)):
            # print('s[i] =', s[i])
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                history_array.append(s[i])
                # print('history_array',history_array)
            else:
                if len(history_array) == 0:
                    return False
                last_opening_bracket = history_array.pop(len(history_array)-1)
                # print('last_opening_bracket',last_opening_bracket)
                if s[i] == ')' and last_opening_bracket != '(':
                    return False
                if s[i] == ']' and last_opening_bracket != '[':
                    return False
                if s[i] == '}' and last_opening_bracket != '{':
                    return False
        
        if len(history_array) != 0:
            return False 
        
        return True
    
solution_obj = Solution()
print(solution_obj.isValid("()"))
print(solution_obj.isValid("()[]{}"))
print(solution_obj.isValid("(]"))
print(solution_obj.isValid("([])"))