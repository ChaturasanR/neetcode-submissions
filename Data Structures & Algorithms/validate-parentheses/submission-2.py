class Solution:
    # T.C: O(N), S.C: O(N)
    char_map = dict({"}": "{", ")" : "(", "]": "["})

    def isValid(self, s: str) -> bool:
        stack = deque()
        for ch in s:
            if ch in self.char_map.values():
                stack.append(ch)
                continue
            
            if ch in self.char_map.keys():
                if not stack or stack.pop() != self.char_map[ch]:
                    return False
                
        return len(stack) == 0

        