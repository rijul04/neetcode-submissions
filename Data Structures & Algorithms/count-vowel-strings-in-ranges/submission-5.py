class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        dic = {word: True if word[0] in vowels and word[-1] in vowels else False for word in words}
        ret = []

        for query in queries:
            start = query[0]
            end = query[1]

            count = 0
            for i in range(start, end+1):
                if dic[words[i]]:
                    count += 1
            
            ret.append(count)
        
        return ret
            