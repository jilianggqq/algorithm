#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import le
from turtle import right
from pandas import pivot


def partition(arr, start, end):
    print("partition start:", start, " end:", end)
    if start >= end:
        return

    print("previous arr:", arr)
    arr2 = arr[start:end+1]
    print("sort part:", arr2)

    index = start
    pivot = arr[start]

    arr[index], arr[end] = arr[end], arr[index]
    while start < end:
        if(arr[start] < pivot):
            arr[start], arr[index] = arr[index], arr[start]
            index = index + 1
        start = start + 1

    arr[index], arr[end] = arr[end], arr[index]
    print("pivot:", pivot)
    print("sorted arr:", arr, ",pivot:", pivot, ",pivot idx:", index, )
    return index


def partition2(arr, start, end):
    print("\nstart:", start, " end:", end)
    print("partition start:", start, " end:", end)
    pivot = arr[start]
    arr[start] = arr[end]
    # end -= 1
    while start < end:
        while start < end and arr[start] <= pivot:
            start += 1
        if start < end:
            arr[end] = arr[start]
            end -= 1
        while start < end and arr[end] >= pivot:
            end -= 1
        if start < end:
            arr[start] = arr[end]
            start += 1
    arr[start] = pivot
    print("pivot:", pivot, ",start:", start, ",arr:", arr)
    return start

# We can assume arr[i+1] >= pivot.
# If arr[j] < pivot, swap(arr[i+1], arr[j])
# if arr[j] >= pivot, j++


def partition3(arr, start, end):
    # this is the python classical version.
    i = start - 1
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[end] = arr[end], arr[i+1]
    # return the pivot index.
    return i+1


def partition4(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1
        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1
        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break
    array[start], array[high] = array[high], array[start]
    return high


def qs(arr, start, end):
    print("\nqs start:", start, " end:", end)
    if start >= end:
        print("start >= end, return")
        return
    p_idx = partition4(arr, start, end)
    qs(arr, start, p_idx - 1)
    qs(arr, p_idx + 1, end)


if __name__ == '__main__':
    # print partition([3, 2, 5, 1], 0, 3)
    a = [6, 7, 32, 32, 1, 8, 5]
    # most time consuming. Sorted array.
    # a = [1, 2, 3, 4, 5, 7, 8]
    print("arr", a)
    qs(a, 0, 6)
    print(a)
