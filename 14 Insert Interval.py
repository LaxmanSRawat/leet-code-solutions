class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        result = []
        to_be_inserted_interval = [None,None]
        for interval in intervals:
            print(interval, to_be_inserted_interval, result, newInterval)
            if to_be_inserted_interval[0] == None:
                if (newInterval[0] >= interval[0]) and (newInterval[0] <= interval[1]):
                    to_be_inserted_interval[0] = interval[0]
                elif (newInterval[0]<interval[0]):
                    to_be_inserted_interval[0] = newInterval[0]
                else:
                    result.append(interval)
            if to_be_inserted_interval[0] != None and to_be_inserted_interval[1] == None:
                if (newInterval[1] >= interval[0]) and (newInterval[1] <= interval[1]):
                    to_be_inserted_interval[1] = interval[1]
                    result.append(to_be_inserted_interval)
                    continue
                elif (newInterval[1] < interval[0]):
                    to_be_inserted_interval[1] = newInterval[1]
                    result.append(to_be_inserted_interval)
                else:
                    continue
            if to_be_inserted_interval[0] != None and to_be_inserted_interval[1] != None:
                result.append(interval)
        if to_be_inserted_interval[0] == None:
            result.append(newInterval)
        elif to_be_inserted_interval[1] == None:
            result.append([to_be_inserted_interval[0],newInterval[1]])
        
        return result
# print(Solution().insert([[1,3],[6,9]],[2,5]))
# print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
# print(Solution().insert([[1,5]],[2,7]))
print(Solution().insert([[1,5]],[0,3]))