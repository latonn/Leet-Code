#

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
# it is able to trap after raining.
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
# section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


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


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))

