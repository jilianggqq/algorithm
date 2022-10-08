#!/usr/bin/env python
# -*- coding: utf-8 -*-

def binarySearch(arr, tg, lo, hi):
    while lo + 1 < hi:
        mid = lo + (hi-lo)//2
        if arr[mid] >= tg:
            hi = mid
        elif arr[mid] < tg:
            lo = mid
    if arr[lo] == tg:
        return lo
    if arr[hi] == tg:
        return hi
    return -1

def linersearch(arr, tg):
    for i in range(len(arr)):
        if tg == arr[i]:
            return i
    return -1

def findMostLeft(arr, target, lo, hi):
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        # move as lo as possible
        if arr[mid] >= target:
            hi = mid
        else:
            lo = mid
    if arr[lo] == target:
        print("return lo index")
        return lo
    if arr[hi] == target:
        print("return hi index")
        return hi
    print("lo", lo, "hi", hi)
    return -1


def findMostRight(arr, target, lo, hi):
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        # move as lo as possible
        if arr[mid] <= target:
            lo = mid
        else:
            hi = mid
    if arr[hi] == target:
        print("return hi index")
        return hi
    if arr[lo] == target:
        print("return lo index")
        return lo
    print("lo", lo, "hi", hi)
    return -1


if __name__ == '__main__':
    print("----------------------findMostLeft----------------------")
    print(findMostLeft([1, 2, 2], 2, 0, 2))
    print(findMostLeft([3, 3, 3, 3, 3, 3, 4], 3, 0, 6))
    print(findMostLeft([1, 2, 3, 5, 6], 4, 0, 4))

    print("----------------------findMostRight----------------------")
    print(findMostRight([1, 2, 2], 2, 0, 2))
    print(findMostRight([3, 3, 3, 3, 3, 3, 4], 3, 0, 6))
    # 7
    print(findMostRight([3, 3, 3, 3, 3, 3, 4, 4], 4, 0, 7))
    print(findMostRight([1, 2, 3, 5, 6], 4, 0, 4))

    print("----------------------binarysearch----------------------")
    print(binarySearch([3, 4, 5, 7, 8], 3, 0, 4))
    print(binarySearch([3, 4, 5, 7, 8], 4, 0, 4))
    print(binarySearch([3, 4, 5, 7, 8], 5, 0, 4))
    print(binarySearch([3, 4, 5, 7, 8], 6, 0, 4))

    print(linersearch([3,5,6], 5))
    print(linersearch([3,5,6], 8))
