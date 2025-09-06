from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        pre2post: list[set[int]] = [set() for _ in range(numCourses)]
        prereq_counts: list[int] = [0 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            pre2post[prereq].add(course)
            prereq_counts[course] += 1

        # All courses with no prerequisites
        queue: deque[int] = deque(course for course, count in enumerate(prereq_counts) if count == 0)
        order: list[int] = []

        while len(queue):
            prereq = queue.popleft()
            order.append(prereq)

            for postreq in pre2post[prereq]:
                prereq_counts[postreq] -= 1
                if prereq_counts[postreq] == 0:
                    queue.append(postreq)

        return order if not any(prereq_counts) else []