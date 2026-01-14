'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.'''

'''Intuition: We can use a hash map to count the occurrences of each letter in the ransomNote and then decrement the counts based on the letters found in the magazine. If all counts reach zero, it means we can construct the ransomNote from the magazine.'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterCount = {}
        for i in ransomNote:
            if i in letterCount:
                letterCount[i] += 1
            else:
                letterCount[i] = 1
        
        for i in magazine:
            if i in letterCount:
                letterCount[i]-=1
                if letterCount[i] == 0:
                    letterCount.pop(i)
        
        return letterCount == {}
        