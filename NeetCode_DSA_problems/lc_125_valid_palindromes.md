# Leetcode 125. 'Valid Palindrome'

## A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Example 1:

Input: s = "A man, a plan, a canal: Panama" </br>
Output: true </br>
Explanation: "amanaplanacanalpanama" is a palindrome. </br>

----
## Given Problem 

if given string is a palindrome then return True else return False</br>

## Idea:

1. Remove the special characters from the string  and convert the string into lowercase.</br>
2. Then reverse the cleaned string and check if both are equal or not. </br>
3. if they are equal then return True else return False </br>

---
## Explanation
Input: s = "A man, a plan, a canal: Panama" </br>
Cleaned_string = "amanaplanacanalpanama" </br>
reverse_string = "amanaplanacanalpanama" </br>
Here both given string (Cleaned_string) and reverse_string are same, so we return True. </br>

# Python Code
```
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_string = ''
        
        for i in s:
            if i.isalnum():
                cleaned_string = cleaned_string + lower(i)

        if cleaned_string==cleaned_string[::-1]:
            return True
        return False
```

