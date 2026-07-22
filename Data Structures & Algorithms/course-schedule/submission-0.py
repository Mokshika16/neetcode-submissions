from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)

        visit = set()
        completed = set()

        def dfs(course):
            if course in visit:
                return False

            if course in completed:
                return True

            visit.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visit.remove(course)
            completed.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True