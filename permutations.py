class Solution(object):
    def helper(self, nums, path, result):
        if not nums:
            result.append(path)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i+1: ], path + [nums[i]], result)
                
        # input: [1,2,3]
        # nums  path
        # [2,3] [1]
        # [1,3] [2]
        # [1,2] [3]
        # Then each of these combinations are backtracked again
                
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path, result = [], []
        if not nums:
            return None
        else:
            self.helper(nums, path, result)
        return result
