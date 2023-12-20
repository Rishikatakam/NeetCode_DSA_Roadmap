# Leetcode 49. 'Group Anagrams' 

## Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]  </br>

Output: [["bat"],["nat","tan"],["ate","eat","tea"]] </br>

----
## Given Problem 

Foe every word in given array, we need to group and segregate the words that have same letters in it. </br>

## Idea:

1. Initialize a defaut dictionary to store the sorted strings and its anagrams </br>
2. for every word, first sort the string then you get the default string. </br>
3. Then for every string in given array, check if it is present in dictionary.  </br>
4. if it is not present, then we need to add that string as key and initialize empty array to store its anagrams </br>
5. if the string is already present, then just add that into respective array. </br>

---

Example: </br>
strs = ["eat","tea","tan","ate","nat","bat"] </br>
1. sorted version of first string "eat" is "aet", add this to dictionary as a key. </br>
2. then add "eat" to it. </br>
3. For "tea", sorted string is "aet" it is already present in dictionary, so add that string to "aet" array.  </br>
Repeat same steps for every other string. </br>

# Python Code
```
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0:
            return [""]
        elif len(strs)==1:
            return [strs]
        res={}
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str not in res:
                res[sorted_str] = []
            
            res[sorted_str].append(i)

        return list(res.values())
```

