class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_of_doubles = 0
        singles = set()
        
        for letter in s:
            if letter in singles:
                count_of_doubles +=2
                singles.remove(letter)
            else:
                singles.add(letter)
        
        if singles:
            return count_of_doubles+1
        else:
            return count_of_doubles