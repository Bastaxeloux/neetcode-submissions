class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        nb_letters = len(set(list(s)))
        print(nb_letters)
        while nb_letters > 0:
            for i in range(len(s)-nb_letters+1):
                window = set(list(s[i:i+nb_letters]))
                if len(window) == nb_letters:
                    return nb_letters
            nb_letters -= 1
        return len(set(list(s)))
