# Leetcode 15. '3Sum'

## Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

---
Example 1:

Input: nums = [-1,0,1,2,-1,-4] </br>
Output: [[-1,-1,2],[-1,0,1]] </br>
Explanation:  </br>
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. </br>
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0. </br>
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. </br>
The distinct triplets are [-1,0,1] and [-1,-1,2]. </br>
Notice that the order of the output and the order of the triplets does not matter. </br>


----
## Given Problem 

We need to find unique combinations of 3 numbers such that sum is equals to 0.</br>

## Idea:

1. Store the negative, positive and zero numbers seperately. </br>
2. Create positive and negative sets to remove duplicate instances from the list. </br>
3. if there are more than 3 zero's in the given list then we can make a combination of all 0's where sum =0. </br>
4. Now find the combination of 2 positive numbers and check if the negavtive number of that sum is present in negative numbers. if it is present then store the new combination. </br>
5. Similar to step 4, check find the combination of 2 negative nubers and check if that sum present in positive set, if it is present then that becomes a new cobination. </br>
6. Return all the combinations. </br>

---
Input: nums = [-1,0,1,2,-1,-4] </br>
negative numbers n = [-1, -1, -4]  </br>
positive numbers p = [1, 2] </br>
zeros z = [0] </br>
P = {1,2}  </br>
N = {-1, -4} </br>
Combinations = [-1,-1,2] , [-1,0,1]  </br>
return result = [[-1,-1,2] , [-1,0,1]] </br>

# Python Code
```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n,p,z=[],[],[]
        res=set()
        for i in nums:
            if i<0:
                n.append(i)
            elif i>0:
                p.append(i)
            else:
                z.append(i)
        N,P=set(n),set(p)

        if z:
            for i in P:
                if -1*i in N:
                    res.add((-1*i,0,i))
        
        if len(z)>=3:
            res.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                temp = -1*(n[i]+n[j])

                if temp in P:
                    res.add((n[i],n[j],temp))
        
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                temp = -1*(p[i]+p[j])
                if temp in N:
                    res.add((p[i],p[j],temp))
        return res




```

