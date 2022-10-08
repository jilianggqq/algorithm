#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cmath import pi
from pandas import pivot


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quickSort(arr, low, high):
    if low >= high:
        return
    pIdx = partition(arr, low, high)
    quickSort(arr, low, pIdx - 1)
    quickSort(arr, pIdx+1, high)


if __name__ == '__main__':
    a = [3, 16, 5, 7, 22]
    quickSort(a, 0, len(a)-1)
    print(a)
