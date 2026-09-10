class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))

        if len(s_list) != len(t_list):
            return False

        for s, t in zip(s_list, t_list):
            if s != t:
                return False

        return True
