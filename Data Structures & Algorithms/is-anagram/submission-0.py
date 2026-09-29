class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countT, countS = {},{}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        for c in s:
            countS[c] = 1 + countS.get(c,0)
        for c in countT:
            if countT[c] != countS.get(c,0):
                return False
        return True




        
        
        