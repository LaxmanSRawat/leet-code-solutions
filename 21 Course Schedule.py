from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        prerequisitesHash = {}
        for prerequisite, course in prerequisites:
            if course not in prerequisitesHash:
                prerequisitesHash[course] = set()
            prerequisitesHash[course].add(prerequisite)
        taken = set()
        print(prerequisitesHash)
        for course in range(0,numCourses):
            if course in taken:
                continue
            result, taken = self.dfs(prerequisitesHash,course,taken, set())
            if not result:
                return result
        return result

    def dfs(self,prerequisitesHash,course, taken, taking):
        print(prerequisitesHash,course, taken, taking)
        if course in taken:
            return True, taken
        
        taking.add(course)

        if course in prerequisitesHash:
            for prerequisite in prerequisitesHash[course]:
                if prerequisite in taking:
                    return False, taken
                result, taken = self.dfs(prerequisitesHash,prerequisite,taken, taking)
                if not result:
                    return result,taken
        taken.add(course)
        taking.remove(course)
        return True, taken


print(Solution().canFinish(4,[[1,0],[2,0],[3,1],[3,2]]))