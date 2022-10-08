from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:

    def helper(nums, res: List[List[int]], temp: List[int], start):
        res.append(temp.copy())
        # temp is a common variable to hold previous values.
        # start means start from which index. That is for the recursion.
        # e.g., [2,2] starts from 0, start is 0, i is in range (0, 2). 
        # Firstly, i is 0, start is 0, put nums[0] into temp, which becomes[2]. Then we can change start to [1], begin the recursion.
        # start becomes 1, i is in range(1,2). i==1 means i==start. temp becomes [1,1]. res.append(temp), then res becomes [[],[1],[1,1]]
        # start is 0 (start == 1 loop is done), i becomes 1. Because i!=start and nums[1] == nums[0], end loop
        for i in range(start, len(nums)):
            if i==start or nums[i] != nums[i-1]:
                temp.append(nums[i])
                print("after append: temp is ", temp, "i=", i, "start=", start)
                helper(nums, res, temp, i+1)
                temp.pop()
                print("after pop: temp is ", temp, "i=", i, "start=", start)

    nums.sort()
    res = []
    helper(nums, res, [], 0)
    return res

res1 = subsetsWithDup([1,2,2])
print(res1)
res1 = subsetsWithDup([0])
print(res1)
res1 = subsetsWithDup([2,2])
print(res1)