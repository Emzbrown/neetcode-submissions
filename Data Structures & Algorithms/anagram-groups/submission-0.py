class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict ={}
        i = 0
        while i < len(strs):
            a = "".join(sorted(strs[i]))
            if a in dict:
                dict[a].append(strs[i])
            else:
                dict[a] = [strs[i]]
            i+=1
        return list(dict.values())