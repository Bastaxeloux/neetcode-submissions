class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for colonne in zip(*strs):
            if len(set(colonne)) != 1:
                break
            i += 1
        return strs[0][:i]