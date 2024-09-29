class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        #Creat result list to  store True/False for each kid
        result = []

        #Find the maximum number of candies among the kids
        max_number_of_candies = max(candies)

        #Making check if  candies + extraCandies >= max_number_of_candies
        for candy in candies:
            if candy + extraCandies >= max_number_of_candies:
                result.append(True)
            else:
                result.append(False)

        return result


