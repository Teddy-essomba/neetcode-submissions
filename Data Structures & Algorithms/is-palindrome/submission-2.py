class Solution:
    def isPalindrome(self, s: str) -> bool:
   
        string = ""
    
        for i in s:
            letter = i.lower()
            if letter.isalnum():
                string += letter
            res = string[::-1]

        if res == string:
            return True
        return False



        