#

# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real
# number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
# where equations.size() == values.size(), and the values are positive. This represents the equations. Return
# vector<double>.
#
# According to the example above:
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
#
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there
# is no contradiction.


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(lambda: defaultdict(int))
        for (i, j), v in zip(equations, values):
            graph[i][j] = v
            graph[j][i] = 1.0 / v
        # print(graph)

        for k in graph:
            graph[k][k] = 1.0
            for i in graph:
                for j in graph:
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = graph[i][k] * graph[k][j]

        result = []
        for i, j in queries:
            result.append(graph[i][j] if graph[i][j] else -1.0)

        return result


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution().calcEquation(equations, values, queries))


