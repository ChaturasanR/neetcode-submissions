class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict(str, List[str]) = defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            print(sorted_str)
            groups[sorted_str].append(string)
        
        return [val for val in list(groups.values())]

        