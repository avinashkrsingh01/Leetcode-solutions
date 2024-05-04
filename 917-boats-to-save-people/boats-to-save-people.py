class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
                ans += 1
            else:
                ans += 1
                j -= 1
        return ans
        