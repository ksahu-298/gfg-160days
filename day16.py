# Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

# Note: You can assume both the strings s1 & s2 are non-empty.
class Solution:
    def areAnagrams(self, s1, s2):
        charCount = {}
        
        for ch in s1:
            charCount[ch] = charCount.get(ch,0) +1
            
        for ch in s2:
            charCount[ch] = charCount.get(ch,0) -1
            
        for value in charCount.values():
            if value != 0:
                return False
        
        return True