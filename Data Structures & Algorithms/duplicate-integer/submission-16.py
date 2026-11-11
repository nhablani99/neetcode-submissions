class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = nums_dict.get(n,0) + 1
            if nums_dict[n] > 1:
                return True
        return False                         
                                      
               
        
                              
    