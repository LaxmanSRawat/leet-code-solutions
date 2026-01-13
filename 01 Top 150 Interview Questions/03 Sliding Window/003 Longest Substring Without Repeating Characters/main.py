'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.'''

'''Intuition: We can use the sliding window technique along with a hash map to keep track of the characters in the current window. We maintain two pointers, left and right, to represent the current substring without repeating characters. As we expand the right pointer, we check if the character is already in the hash map. If it is, we move the left pointer to the right of the previous occurrence of that character to ensure all characters in the current window are unique. We update the maximum length of the substring found during this process.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        r = 0
        pos = {}
        while(r<len(s)):
            if s[r] in pos and pos[s[r]]>=l:
                max_len = max(max_len,r-l)
                l = pos[s[r]]+1
            pos[s[r]] = r
            r+=1
        max_len = max(max_len,r-l)
        return max_len
