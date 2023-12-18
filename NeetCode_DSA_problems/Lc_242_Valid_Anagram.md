# Leetcode 242 'Valid Anagram' 

## Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
</br>

Example 1:

Input: s = "anagram", t = "nagaram" </br>
Output: true

----
## Given Problem 

we have to check if we can build 't' by rearranging the letters in 's'. 

## Idea:

1.convert the string into list </br>
2.sort the list </br>
3. check if elements in both lists are equal or not. </br>
4. if they are equal, return True </br>
5. else return False </br>

We can use 'sorted' method to do this.
---

Example: </br>
s = "anagram", t = "nagaram" </br>
sorted(s) = [u'a', u'a', u'a', u'g', u'm', u'n', u'r'] </br>
sorted(t) = [u'a', u'a', u'a', u'g', u'm', u'n', u'r'] </br>
Here sorted(s) is equal to sorted(t) </br>

# Python Code
```
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s)==sorted(t):
            return True
        return False
        
```

