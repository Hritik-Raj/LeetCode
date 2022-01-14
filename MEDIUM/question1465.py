class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalStrips = [0] + sorted(horizontalCuts) + [w]
        verticalStrips = [0] + sorted(verticalCuts) + [h]
        
        maxW = max([horizontalStrips[i+1] - horizontalStrips[i] for i in range( len(horizontalStrips) - 1)])
        maxH = max([verticalStrips[i+1] - verticalStrips[i] for i in range(0, len(verticalStrips) - 1)])
        
        return (maxH * maxW) % ((10 ** 9) + 7)