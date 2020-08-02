# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# // Time Complexity : o(n)
# // Space Complexity : o(1)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : None
#
#
# // Your code here along with comments explaining your approach

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = nums[i]
            if temp < 0:
                temp *=-1
            if nums[temp-1] > 0:
                nums[temp-1]*=-1
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result