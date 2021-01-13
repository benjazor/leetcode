# NAME : Boats to Save People
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/
# DATE : 13/01/2021

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        left = 0
        right = len(people) - 1
        result = 0
        
        while (left <= right):
            print(people[left], people[right])
            if (people[left] + people[right] <= limit):
                left += 1
            right -= 1
            result += 1
            
        return result
