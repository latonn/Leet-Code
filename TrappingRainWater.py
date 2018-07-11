class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lefthigh = [0 for _ in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            lefthigh[i] = leftmax
        sum = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
                rightmax = height[i]
            if min(rightmax, lefthigh[i]) > height[i]:
                sum += min(rightmax, lefthigh[i]) - height[i]
        return sum