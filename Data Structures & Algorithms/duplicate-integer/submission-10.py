class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count_dict = {}
        

        for n in nums:
            count_dict[n] = 1 + count_dict.get(n,0)

        for value in count_dict.values():
            if value >= 2:
                return True

        return False        
        
                              

        