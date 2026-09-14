class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = [str(len(word)) + "@" + word for word in strs]

        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        print("s: ", s)
        strs = []

        index = 0
        while(index < len(s)):
            str_count = ""
            for i in range(index, len(s)):
                index += 1
                if s[i] == "@":
                    break
                str_count += s[i]
            print("str_count: ", str_count)
            word = ""
            for i in range(index, index+int(str_count)):
                word += s[i]
                index += 1
            
            print("word: ", word)
            strs.append(word)
        
        return strs
