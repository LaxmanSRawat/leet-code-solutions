'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.'''

'''
intuition: To determine if two strings are isomorphic, we can use two hash maps (dictionaries) to keep track of the character mappings from string s to string t and from string t to string s. As we iterate through the characters of both strings simultaneously, we check if the current character from s has already been mapped to a different character in t or vice versa. If we find any inconsistencies in the mappings, we return false. If we complete the iteration without finding any issues, we return true, indicating that the strings are isomorphic.'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map_s = {}
        char_map_t = {}
        for index, char in enumerate(s):
            if (char in char_map_s and char_map_s[char] != t[index]) or (t[index] in char_map_t and char_map_t[t[index]] != char):
                return False
            char_map_s[char] = t[index]
            char_map_t[t[index]] = char
        return True