# Time:  O(n * sqrt(n))
# Space: O(n)

# Suppose you have a random list of people standing in a queue.
# Each person is described by a pair of integers (h, k), where
# h is the height of the person and k is the number of people
# in front of this person who have a height greater than or
# equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopleDict, height, result = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopleDict:
                peopleDict[p[0]] += (p[1], i),
            else:
                peopleDict[p[0]] = [(p[1], i)]
                height += p[0],

        print(peopleDict)
        print(height)

        height.sort()  # here are different heights we have
        print(height)

        # sort from the tallest group
        for h in height[::-1]:
            print("h: ", h)
            peopleDict[h].sort()
            print(peopleDict[h])
            for p in peopleDict[h]:
                print(p, p[1])
                result.insert(p[0], people[p[1]])
                print("result per iteration: ", result)

        return result

        # latonn's
        # Time:  O(n^2)
        # Space: O(n)
        # people.sort(key=lambda h_k: (-h_k[0], h_k[1]))
        # print(people)
        # result = []
        # for p in people:
        #     result.insert(p[1], p)
        #     print(result)
        # return result

        # kamyu's
        # people.sort(key=lambda h_k: (-h_k[0], h_k[1]))
        #
        # blocks = [[]]
        # for p in people:
        #     index = p[1]
        #
        #     # print(enumerate(blocks))
        #     for i, block in enumerate(blocks):
        #         print(i, block)
        #         if index <= len(block):
        #             break
        #         index -= len(block)
        #     block.insert(index, p)
        #     # print(i)
        #
        #     if len(block) * len(block) > len(people):
        #         print("test")
        #         print(i)
        #         blocks.insert(i + 1, block[len(block) / 2:])
        #         del block[len(block) / 2:]
        #
        # return [p for block in blocks for p in block]


if __name__ == '__main__':
    # people = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(people))
