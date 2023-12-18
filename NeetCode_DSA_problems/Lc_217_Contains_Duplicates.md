# Leetcode 317 'Contains Duplicates' 

## Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true

Given array contains '1' two times. At index 0 and 3.

----

## Idea:

1.Convert the Array into a set and check the length of set and given array

1.1. if length is same, then return False
1.2. else return True

Example:
nums = [1,2,3,1]
1.set(nums) = ([1,2,3])
len(nums) = 4
len(set(nums)) = 3

Here, len(nums) not equals to len(set(nums)). 
So, this tells us there is a duplicate element/s in the given array.

# Python Code
```
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        return True
```


