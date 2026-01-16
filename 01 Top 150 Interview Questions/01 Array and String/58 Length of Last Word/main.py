'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.'''


'''intuition: We can iterate through the string from the end to the beginning, counting the length of the last word until we encounter a space. If we encounter spaces at the end, we skip them until we find the last word.'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(1,len(s)+1):
            if s[-i] == " " and count > 0:
                return count
            if s[-i] != " ":
                count+=1
        return count