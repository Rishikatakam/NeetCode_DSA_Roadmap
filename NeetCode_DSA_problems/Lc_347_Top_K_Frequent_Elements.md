# Leetcode 347. 'Top K Frequent Elements'

## Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

---
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2 </br>
Output: [1,2] </br>

----
## Given Problem 

We need to find the frequency of all elements and return the top most k frequent elements </br>

## Idea:

1. Store the frequency of elements in dictionary </br>
2. Sort the dictionary based on key using sorted function. This function returns a list. </br>
3. extarct and store the top k keys and return them. </br>

---
Input: nums = [1,1,1,2,2,3], k = 2 </br>
Frequency of elements stored in a dictionary. {1: 3, 2: 2, 3: 1} </br>
Sorted dictionary, stored as a list [(1, 3), (2, 2), (3, 1)] </br>
Top 2 frequent elemnts are : [1,2] </br>
return [1,2] </br>

# Python Code
```
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count={}
        keys=[]
        for i in nums:
            if i not in count.keys():
                count[i]=0
            count[i] +=1
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for i in sorted_count:
            keys.append(i[0])

        return keys[:k]
```

