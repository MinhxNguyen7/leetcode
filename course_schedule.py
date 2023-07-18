from collections import deque

# See also:
#https://leetcode.com/problems/course-schedule/solutions/441722/python-99-time-and-100-space-collection-of-solutions-with-explanation/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre2post: list[set[int]] = [set() for _ in range(numCourses)]
        in_degrees: list[int] = [0 for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            pre2post[prerequisite].add(course)
            in_degrees[course] += 1
        
        queue: deque[int] = deque()

        for course, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                queue.append(course)
        
        while len(queue):
            prereq = queue.popleft()

            for course in pre2post[prereq]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    queue.append(course)

        return not any(in_degrees)
    
if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0]]))