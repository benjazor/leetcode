# NAME : Course Schedule III
# LINK : https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3729/
# DATE : 03/05/2021

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap, total = [], 0
        for duration, end in sorted(courses, key=lambda elem: elem[1]):
            if duration + total <= end:
                total += duration
                heappush(heap, -duration)

            elif heap and -heap[0] > duration:
                total += duration + heappop(heap)
                heappush(heap, -duration)

        return len(heap)
