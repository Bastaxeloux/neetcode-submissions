class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = []
        l_min = min([len(s) for s in strs])
        i = 0
        ajout = True
        while ajout and i < l_min :
            c = strs[0][i]
            for s in strs[1:]:
                if not c == s[i]:
                    ajout = False
            if ajout :
                out.append(c)
            i += 1
        return "".join(out)
        
        