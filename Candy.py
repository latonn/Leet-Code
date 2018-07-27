class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings)==0:
            return 0
        candies=[1 for index in range(len(ratings))]
        for index in range(1,len(ratings)):
            if ratings[index]>ratings[index-1]:
                candies[index]=candies[index-1]+1
        for index in reversed(range(1,len(ratings))):
            if ratings[index]<ratings[index-1]:
                candies[index-1]=max(candies[index]+1,candies[index-1])
        return sum(candies)

