# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)

# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat", "tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.

import collections


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # kamyu's
        anagrams_map, result = collections.defaultdict(list), []
        for s in strs:
            sorted_str = "".join(sorted(s))
            anagrams_map[sorted_str].append(s)
        print(anagrams_map)
        for anagram in anagrams_map.values():
            # print(anagram)
            anagram.sort()
            result.append(anagram)
        return result


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
