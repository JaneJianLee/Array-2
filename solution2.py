## Problem2
#Given an array of numbers of length N, find both the minimum and maximum. Follow up : Can you do it using less than 2 * (N - 2) comparison
#given nums = [1,7,1,2,3,8,0] , find min and max with less than 2n-2 comparison

# Comparison : for every two elements, we are doing 3 comparisons --> 3*n/2

compare_count = 0
class Solution:
    def findMinMax(self, nums, start, end):
        global compare_count
        # termination
        if end-start == 0:
            return (nums[start], nums[start])
        elif end-start == 1:
            compare_count += 1
            if nums[start]>=nums[end]:
                return (nums[end], nums[start])
            return (nums[start], nums[end])
        else:
            mid = int(start+(end-start)/2)
            result_left = self.findMinMax(nums,start,mid)
            result_right = self.findMinMax(nums,mid+1,end)

        #get MIN:
        minimum = result_left[0] if result_left[0] < result_right[0] else result_right[0]
        compare_count += 1

        #get MAX:
        maximum = result_left[1] if result_left[1] > result_right[1] else result_right[1]
        compare_count += 1

        return (minimum,maximum)
test = [
    [3],
    [3,4],
    [3, 4, 2, 6] ,
    [3, 4, 2, 6, 8],
    [3, 4, 2, 6, 8, 1, 9, 12],
    [3, 4, 2, 6, 8, 1, 9, 12,15],
    [3, 4, 2, 6, 8, 1, 9, 12, 15, 11],
    [3, 4, 2, 6, 8, 1, 9, 12, 15, 11,3, 4, 2, 6, 8, 1, 9, 12, 15, 11]
]
def main():
    global test
    global compare_count
    for num in test:
        start= 0
        end = len(num)-1
        sol=Solution()
        final=sol.findMinMax(num,start,end)
        print(final)
        print("n: ",len(num), " compare count", compare_count)
        compare_count =0

main()

