class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map to store character frequency and the list of words with same character freq
        # anagrams will have same frequency for all characters
        groups: dict(tuple, List[str]) = defaultdict(list) 

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            groups[tuple(count)].append(string)
        
        return list(groups.values())

        