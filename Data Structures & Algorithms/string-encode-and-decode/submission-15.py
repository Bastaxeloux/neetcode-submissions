class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#"*10
        encoded = ";".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "#"*10:
            return []
        decoded = s.split(";")
        return decoded