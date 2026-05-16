class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(w)}#{w}" for w in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            pos_s = s.find("#",i)
            lenght = int(s[i:pos_s])
            next_block = pos_s + 1 + lenght
            word = s[pos_s+1:next_block]
            decoded.append(word)
            i = next_block
        return decoded
            