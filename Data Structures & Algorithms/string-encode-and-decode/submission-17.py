class Solution:
    
    def encode(self, strs: List[str]) -> str:
        print(len(strs))
        return "-!".join(word for word in strs) if len(strs) > 0 else "None"

    def decode(self, s: str) -> List[str]:
        return s.split("-!") if s != "None" else []
