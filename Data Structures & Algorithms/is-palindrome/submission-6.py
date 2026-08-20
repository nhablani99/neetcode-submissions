class Solution:
    def isPalindrome(self, s: str) -> bool:
              new_string = "".join(ch.lower() for ch in s if ch.isalnum())
              return new_string.lower() == new_string.lower()[::-1]

                 
                


        
     
        