class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        ret = []

        for query in queries:
            start = query[0]
            end = query[1]

            count = 0
            for i in range(start, end+1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    count += 1
            
            ret.append(count)
        
        return ret
            