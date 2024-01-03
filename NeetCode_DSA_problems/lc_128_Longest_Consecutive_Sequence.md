# Leetcode 128. 'Longest Consecutive Sequence'

## Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:

Input: nums = [100,4,200,1,3,2] </br>
Output: 4 </br>
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].</br>  Therefore its length is 4.</br>

----
## Given Problem 

We need to find the longest consecutive sequence in the given array and return the count.</br>

## Idea:

1. Sort the numbers  </br>
2. For index i, check if number at i-1 is same, if it is same then we can ignore that number and proceed further</br>
3. check if number at i is equals to '(number at i-1) + 1', this tells us that numbers are consecutive.</br>
4. Increase the count by 1 everytime we encounter a consecutive number.
5. if number at i is not consecutive, then update the max_count and initialize the count to 1.
6. After every iteration, update the max_count

---
Input: nums = [100,4,200,1,3,2] </br>
Sorted array = [1,2,3,4,100,200] </br>
max_count = 4 </br>
return 4 (max count) </br>

# Python Code
```
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        count=1
        sorted_nums= sorted(nums)
        if len(nums)==1:
            return 1 
        for i in range(1,len(nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                max_count=max(max_count,count)
                continue
            if sorted_nums[i] == sorted_nums[i-1]+1:
                count=count+1
            else:
                max_count=max(max_count,count)
                count=1
            max_count=max(max_count,count)

        return max_count
```

