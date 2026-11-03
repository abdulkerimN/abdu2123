
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0

        for number in nums:
            answer = answer ^ number

        return answer
