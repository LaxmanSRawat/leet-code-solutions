class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        
        
        history = {}
        history[0] = set()
        history[0].add(("0 "*len(candidates)).strip())

        for current_val in range(1,target+1):
            for candidate_index in range(0,len(candidates)):
                candidate= candidates[candidate_index]
                if candidate > current_val:
                    continue
                
                if current_val - candidate in history:
                    if current_val not in history:
                        history[current_val] = set()

                    for combination in history[current_val-candidate]:
                        if current_val == target:
                            print(current_val,candidate,combination)
                        temp = combination.split(' ')
                        temp[candidate_index] = str(int(temp[candidate_index]) + 1)
                        temp = ' '.join(temp)
                        # temp = combination[:candidate_index] + str((int(combination[candidate_index]) + 1)) +combination[candidate_index+1:]
                        if current_val == target:
                            print(temp)
                        history[current_val].add(temp)

        result = []
        if target in history:
            for i in history[target]:
                temp = []
                count = 0
                for j in i.split(' '):
                    if j == '0':
                        count+=1
                        continue
                    temp = temp + [candidates[count]]*int(j)
                    count+=1
                result.append(temp)
        return result


print(Solution().combinationSum([18,34,2,16,25,6,35],20))