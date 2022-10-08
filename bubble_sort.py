#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bub_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            # if
        # for
    # for
    return arr


bub_sort([3, 2, 5, 6, 22, 2])
