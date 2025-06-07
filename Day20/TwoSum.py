class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        i = 0
        while i < length - 1:
            j = i + 1
            while j < length:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
        return []  

nums = list(map(int, input().split()))
target = int(input())
a = Solution()
print(a.twoSum(nums, target))
