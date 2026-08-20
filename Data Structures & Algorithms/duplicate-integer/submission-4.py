class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_list = []
        for num in nums:
            if num in empty_list:
                return True
            else:
                empty_list.append(num)
        return False                                  

                
         