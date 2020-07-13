#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:52:31 2020

@author: michael
"""

def bubble_sort(numbers):
    arr = numbers[:]
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
    
x = [5, 1, 14, 9, 36, -6, 14, .2, 7, 0 , 7, 51, 2, 4]

print(bubble_sort(x))