# 167. Two Sum II - Input Array Is Sorted

## Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

---
Example 1:

Input: numbers = [2,7,11,15], target = 9 </br>
Output: [1,2] </br>
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]. </br>

----
## Given Problem 
Given a sorted list (descending order) and a target value, we need to return indices of 2 numbers such that sum of those two numbers is equal to target. </br>

we cannot use the same number again.

## Idea:
*Two Pointer solution* </br>
1. initialize two variables i and j. Assign i to 0 left most index of the array and j to length of array -1, i.e right most index of the array. </br>
2. Now check if number at i + number at j is equal to target, if yes return i+1,j+1 because index of given array starts from 1.</br>
3. if sum is < target then increment i. </br>
4. if sum is > target then decrement j. </br>

---
## Explanation
Input: numbers = [2,7,11,15] , Target = 9 </br>
Value at i=0 is 2, and value at j=len(arr)-1 is 15. So sum = 17 </br>
Sum is > 9 (target). Therefore decrement j. </br>
new sum = 2+11 = 13. 13>9. Therefore again decrement j. </br>
Sum = 2+7 = 9 == target value 9, There fore return [i+1,j+1] = [1,2] </br>
Output = [1,2] </br>

# Python Code
```
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j=0,len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j] == target:
                return i+1,j+1
            elif numbers[i]+numbers[j] < target:
                i=i+1
            else:
                j=j-1    
```

