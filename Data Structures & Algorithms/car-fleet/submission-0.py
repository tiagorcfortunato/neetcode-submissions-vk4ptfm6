class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []  
        for p, s in pairs:                             
            if not stack or (target - p) / s > stack[-1]:
                stack.append((target - p) / s)
                                                                                                        
        return len(stack)