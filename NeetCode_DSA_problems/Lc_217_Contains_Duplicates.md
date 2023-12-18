# Leetcode 317 'Contains Duplicates' 

## Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1] </br>
Output: true

Given array contains '1' two times. At index 0 and 3.

----
## Given Problem 

we have to check if given array contains duplicate numbers or not. if it contains then return True else return False.

## Idea:

1.Convert the Array into a set and check the length of set and given array </br>
2. if length is same, then return False </br>
3. else return True

---

Example: </br>
nums = [1,2,3,1] </br>
1.set(nums) = ([1,2,3]) </br>
len(nums) = 4 </br>
len(set(nums)) = 3 </br>

Here, len(nums) not equals to len(set(nums)).  </br>
So, this tells us there is a duplicate element/s in the given array. </br>

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


