class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
        return []


twosum = Solution()
result = twosum.twoSum([2, 7, 11, 15], 9)
print(result)
