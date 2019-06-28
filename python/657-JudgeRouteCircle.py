#

# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
# which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are
# R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a
# circle.
#
# Example 1:
# Input: "UD"
# Output: true
#
# Example 2:
# Input: "LL"
# Output: false


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # latonn's
        m = [0 for _ in range(4)]
        for move in moves:
            if move == 'U':
                m[0] += 1
            elif move == 'D':
                m[1] += 1
            elif move == 'L':
                m[2] += 1
            else:
                m[3] += 1
        return m[0] == m[1] and m[2] == m[3]


if __name__ == '__main__':
    moves = "LDRRLRUULR"
    print(Solution().judgeCircle(moves))
