#!/usr/bin/env python
# -*- coding: utf-8 -*-

from importlib_metadata import re


def findDuplicate(nums):
    res = set()
    tmp = set()
    for num in nums:
        if num in tmp:
            res.add(num)
        else:
            tmp.add(num)
    return list(res)

def findDuplicate2(nums):
    ln = len(nums)
    tmp = [-1] * ln
    for num in nums:
        # num not in tmp
        if tmp[num] == -1:
            tmp[num] = -2;
        elif tmp[num] == -2:
            # duplicate element
            tmp[num] = -3;
    res = [];
    for i in range(ln):
        if tmp[i] == -3:
            res.append(i)
    return res

# time complesity O(n)
# space complesity O(n)
def findDuplicateNumber(nums):
    n = len(nums)
    alist = [-1]*n
    clist = []
       # cSet = {}
    for num in nums:
        if alist[num] == -1:
            alist[num] = -2
        elif alist[num] == -2:
            alist[num] = -3

    # loop a list, get idx which value is -3
    for i in range(n):
        if alist[i] == -3:
            clist.append(i)
    return clist

def findDuplicateNumber4(nums):
    res = set()
    n = len(nums)
    for ele in nums:
        e = abs(ele)
        if e == n:
            e = 0
        if nums[e] > 0:
            nums[e] *= -1
        elif nums[e] < 0 or nums[e] == n:
            res.add(e)
        else:
            nums[e] = n
    return list(res)

def findDuplicateNumber5(nums):
    res = set()
    n = len(nums)
    for ele in nums:
        e = ele - n if ele >= n else ele
        if nums[e] < n:
            nums[e] += n
        else:
            res.add(e)
    return list(res)


if __name__ == '__main__':
    arry = [1, 3, 3, 3, 2, 2, 5, 5, 5, 6]
    print(findDuplicateNumber5(arry))
    arry = [0]
    print(findDuplicateNumber5(arry))
    arry = [1, 2, 2]
    print(findDuplicateNumber5(arry))
    arry = [1, 0, 2]
    print(findDuplicateNumber5(arry))
    # error case
    # arry = [1, 2, 3]
    # print(findDuplicateNumber(arry))
    
