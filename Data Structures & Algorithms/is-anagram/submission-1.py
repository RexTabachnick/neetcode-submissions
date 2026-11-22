class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        wordS = {}
        wordT = {}

        for letter in s:
            wordS[letter] = wordS.get(letter, 0) + 1
        for letter in t:
            wordT[letter] = wordT.get(letter, 0) + 1

        for key in wordS:
            if wordT.get(key) != wordS.get(key):
                return False
        
        for key in wordT:
            if wordT.get(key) != wordS.get(key):
                return False

        return True
        

        
        
