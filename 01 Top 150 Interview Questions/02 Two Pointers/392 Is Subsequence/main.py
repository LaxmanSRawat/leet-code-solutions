'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?'''

'''Intuition: We can use two pointers to traverse both strings. One pointer will iterate through string s and the other through string t. Whenever we find a matching character in both strings, we move the pointer in s forward. If we reach the end of s, it means all characters in s were found in t in order, and we return true. If we finish iterating through t without finding all characters of s, we return false. This approach has a time complexity of O(n), where n is the length of t.'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        pt = 0

        while(ps<len(s) and pt<len(t)):
            if s[ps] == t[pt]:
                ps+=1
            pt+=1
            
        if ps == len(s):
            return True
        return False