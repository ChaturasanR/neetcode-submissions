class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map to store character frequency and the list of words with same character freq
        # anagrams will have same frequency for all characters
        # T.C: O(M*N*26) ~ O(M*N), M = number of strings, N = max number of characters in the string
        # S.C: O(26*M*N) = O(M*N), auxilary: O(M)
        groups: dict(tuple, List[str]) = defaultdict(list) 

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            groups[tuple(count)].append(string)
        
        return list(groups.values())

        