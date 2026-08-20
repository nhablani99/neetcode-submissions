class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict_of_S, dict_of_T = {},{}
            for i in range(len(s)):
                dict_of_S[s[i]] = 1 + dict_of_S.get(s[i],0)
                dict_of_T[t[i]] = 1 + dict_of_T.get(t[i],0)
        return dict_of_S == dict_of_T        
                   
        