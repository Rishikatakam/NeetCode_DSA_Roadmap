# Leetcode 1. 'Two Sum' 

## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---
Example 1:

Input: nums = [2,7,11,15], target = 9 </br>
Output: [0,1] </br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. </br>

----
## Given Problem 

we have to check if given array contains numbers that add upto given target value and both numbers should have different index.

## Idea:

1. Check if target-current value is present in given array.  </br>
2. if yes then check if index of both numbers is different. </br>
3. if yes, then return the index of both numbers in an array format. </br>

---

Example: </br>
nums = [2,7,11,15], target = 9</br>
1.9-2 =7, check if 7 present in nums, Yes it is present. </br>
2. check if index of 2 and 7 are different, Yes they are different. 2 is located at index 0 and 7 is located at index 1.</br>
3. So, return [0,1] </br>


# Python Code
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums and nums.index(target-nums[i])!=i:
                return [i,nums.index(target-nums[i])]
```

