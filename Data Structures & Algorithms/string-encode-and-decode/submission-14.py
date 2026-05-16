class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#"*20
        encoded = ";".join(strs)
        print("encoded = ",encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "#"*20:
            return []
        print("s = ",s)
        decoded = s.split(";")
        print("decoded = ",decoded)
        return decoded