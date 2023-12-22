# Leetcode 238. 'Product of Array Except Self'

## Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

---
Example 1:

Input: nums = [1,2,3,4] </br>
Output: [24,12,8,6] </br>

----
## Given Problem 

we need to find the product of all the numbers present in given array except self. </br>

## Idea:

Output of a number is multiplication of prefix and postfix. </br>
1. calculate the multiplication of every numer left to the current number.  (prefix) </br>
2. Then in reverse order calculate the postfix and multiply it with prefix. </br>
   
---

Example: </br>
Input: nums = [1,2,3,4]  </br>
prefix: [1, 1, 2, 6]  </br>
result after multiplying with postfix: [24, 12, 8, 6]  </br>

# Python Code
```
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]*len(nums)
        post=1
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]

        for i in reversed(range(len(nums))):
            res[i]=res[i]*post
            post=post*nums[i]

        return res

```

