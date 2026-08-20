class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beginning = 0
        end = len(nums)
        while beginning < end:
            mid = (beginning + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                beginning = mid + 1
        return -1                

        