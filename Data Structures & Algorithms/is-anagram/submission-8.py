class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 1:
            return s == t
        else:
            count_dict_s = {}
            count_dict_t = {}
            for c in s:
                count_dict_s[c] = 1 + count_dict_s.get(c,0)
            for a in t:
                count_dict_t[a] = 1 + count_dict_t.get(a,0)

            return count_dict_s == count_dict_t        

                   
        