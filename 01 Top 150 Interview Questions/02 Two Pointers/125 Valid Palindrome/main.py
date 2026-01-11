'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.'''

'''Intuition: We can use two pointers, one starting from the beginning of the string and the other from the end. We move the pointers towards each other, skipping non-alphanumeric characters. At each step, we compare the characters at the two pointers (after converting them to lowercase). If they are not equal, we return false. If the pointers cross each other, we return true. This approach ensures that we only traverse the string once, resulting in O(n) time complexity and O(1) space complexity.'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        r= len(s)-1
        l= 0

        
        while(l<r):
            left = s[l].lower()
            right = s[r].lower()
            if (not left.isalnum()):
                l+=1
            elif (not right.isalnum()):
                r-=1
            else:
                if left != right:
                    return False
                else:
                    l+=1
                    r-=1
        return True