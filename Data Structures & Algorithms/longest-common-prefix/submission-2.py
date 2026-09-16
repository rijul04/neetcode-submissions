class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        c_p = strs[0] if len(strs) > 0 else ""
        for word in strs:
            if word[ :len(c_p)] == c_p:
                continue
            
            while word[ :len(c_p)] != c_p:
                c_p = c_p[ :-1]
                if len(c_p) == 0:
                    break
            
        return c_p