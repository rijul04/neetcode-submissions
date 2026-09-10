class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # count = 0
        # allowed = list(allowed)
        # for word in words:
        #     is_fine = True
        #     for c in word:
        #         if c not in allowed:
        #             is_fine = False

        #     if is_fine:
        #         count += 1

        # return count

        count = 0
        allowed_set = set(list(allowed))

        for word in words:
            word_set = set(list(word))
            if word_set <= allowed_set:
                count += 1

        return count