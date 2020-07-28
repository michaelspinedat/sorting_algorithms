#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:52:31 2020

@author: michael
"""

import math

x = [5, 1, 14, 9, 36, -6, 14, .2, 7, 0 , 7, 51, 2, 4]

def bubble_sort(arr):    
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]    
    
print("Bubble sort")
print(x)
copy = x[:]
bubble_sort(copy)
print(copy)

#-------------------------------------------------------
def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

def get_minimum(arr, start):
    minimum = arr[start]
    index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            index = i
    return index

def selection_sort(arr):    
    for i in range(0, len(arr) - 1):
        index = get_minimum(arr, i + 1)
        if arr[index] < arr[i]:
            swap(arr, i, index)    

print("Selection sort")
print(x)
copy = x[:]
selection_sort(copy)
print(copy)

#-------------------------------------------------------

def insert(array, index, value):  
    i = index
    while i >= 0 and array[i] > value:
        array[i + 1] = array[i]
        i -= 1
    array[i + 1] = value

def insertion_sort(arr):    
    for i in range(0, len(arr) - 1):
        insert(arr, i, arr[i + 1])    
        
print("Insertion sort")
print(x)
copy = x[:]
insertion_sort(copy)
print(copy)

#-------------------------------------------------------

def merge(array, p, q, r):
    
    k = p
    i = 0
    j = 0
    lowHalf = [None]*(q - k + 1)

    while k <= q:
        lowHalf[i] = array[k]
        i += 1
        k += 1

    highHalf = [None]*(r - k + 1) 
    while k <= r:
        highHalf[j] = array[k]
        j += 1
        k += 1
    
    k = p
    i = 0
    j = 0

    while i < len(lowHalf) and j < len(highHalf):
        if lowHalf[i] <= highHalf[j]:
            array[k] = lowHalf[i]
            i += 1
        else:
            array[k] = highHalf[j]
            j += 1
        k += 1

    while i < len(lowHalf):
        array[k] = lowHalf[i]
        i += 1
        k += 1

    while j < len(highHalf):
        array[k] = highHalf[j]
        j += 1
        k += 1

def merge_sort(array, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)

print("Merge sort")
print(x)
copy = x[:]
merge_sort(copy, 0, len(copy) - 1)
print(copy)
