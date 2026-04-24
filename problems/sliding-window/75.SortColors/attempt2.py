class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, 0
       
        if len(nums) == 1:
            return 
        for _ in range(len(nums)):
            l, r = 0, 0
            while  r < len(nums): 
                r = l + 1
                if nums[l] >= nums[r]:
                    temp = nums[l]
                    nums[l] = nums[r]
                    nums[r] = temp
                l +=1 
                r += 1

solution = Solution()
p = [2,0,2,1,1,0]
# [0, 2,2,1,1,0]
# [0, 2,1,2,1,0]
# [0, 2,1,1,2,0]
# [0, 2,1,1,0,2]
p2 = [2, 0 ,1]
p3 = [2, 0 ,1, 1, 2,2,1,2]
p4 = [2, 0]
print(solution.sortColors(p))
print(solution.sortColors(p2))
print(solution.sortColors(p3))
print(solution.sortColors(p4))

print(p)
print(p2)
print(p3)
print(p4)

