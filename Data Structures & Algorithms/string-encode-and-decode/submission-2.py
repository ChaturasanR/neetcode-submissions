# Note: Not able to do on my own
# Intituition is that simple character delimiter won't work, we need to store length
# and use that length to decode
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = []
        for string in strs:
            str_length = len(string)
            res.append(str(str_length))
            res.append('#')
            res.append(string)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            s_len = int(s[i:j])
            i = j + 1
            j = i + s_len
            res.append(s[i: j])
            i = j
        return res


