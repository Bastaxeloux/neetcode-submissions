def isAnagram(str1,str2):
    if len(str1) != len(str2):
        return False
    dict1, dict2 = {}, {}
    for i in range(len(str1)):
        dict1[str1[i]] = dict1.get(str1[i],0) + 1
        dict2[str2[i]] = dict2.get(str2[i],0) + 1
    return dict1 == dict2

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        for word in strs:
            found=False
            if len(grouped)==0:
                grouped.append([word])
            else:
                for i,elmt in enumerate(grouped):
                    if isAnagram(word,elmt[0]):
                        found=True
                        grouped[i].append(word)
                if not found:
                    grouped.append([word])
        return grouped
        