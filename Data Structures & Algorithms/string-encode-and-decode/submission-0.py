class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""    
        for x in strs:                                                                            
          res += str(len(x)) + "#" + x
        return res 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
          j = s.index("#", i)                                                                   
          length = int(s[i:j])
          word = s[j + 1: j + 1 + length]                                                       
          res.append(word)
          i = j + 1 + length
        return res