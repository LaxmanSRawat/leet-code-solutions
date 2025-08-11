class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_s = {}
        hashmap_t = {}
        if(len(s) != len(t)):
            return False
        for i in range(0,len(s)):
            if s[i] in hashmap_s:
                hashmap_s[s[i]]+=1
            else:
                hashmap_s[s[i]]=1
            if t[i] in hashmap_t:
                hashmap_t[t[i]]+=1
            else:
                hashmap_t[t[i]]=1
        if(len(hashmap_t) != len(hashmap_s)):
            return False
        else:
            for i in hashmap_s:
                if (i not in hashmap_t) or (hashmap_s[i] != hashmap_t[i]):
                    return False
        return True
    
solution_obj = Solution()
print(solution_obj.isAnagram("anagram","nagaram"))
print(solution_obj.isAnagram("rat","car"))
print(solution_obj.isAnagram("t","r"))
print(solution_obj.isAnagram("laxman","namxal"))
                
        