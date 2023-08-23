class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i = 0
        j = len(height) - 1
        while (i < j):
            tmp = 0
            if (height[i] > height[j]):
                tmp = (height[i] + height[j] + height[j] - height[i])/2 * (j-i)
                j -= 1
            elif (height[i] < height[j]):
                tmp = (height[i] + height[j] + height[i] - height[j])/2 * (j-i)
                i += 1
            else:
                tmp = (height[i] + height[j]) / 2 * (j - i)
                i += 1
            area = max(area,int(tmp))
        return area
