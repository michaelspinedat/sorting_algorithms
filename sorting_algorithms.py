#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:52:31 2020

@author: michael
"""

x = [5, 1, 14, 9, 36, -6, 14, .2, 7, 0 , 7, 51, 2, 4]

def bubble_sort(numbers):
    arr = numbers[:]
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

    
print("Bubble sort")
print(x)
print(bubble_sort(x))
print()


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
    new_arr = arr[:]
    for i in range(0, len(new_arr) - 1):
        index = get_minimum(new_arr, i + 1)
        if new_arr[index] < new_arr[i]:
            swap(new_arr, i, index)      
    return new_arr

print("Selection sort")
print(x)
print(selection_sort(x))
print()
#-------------------------------------------------------

def insert(array, index, value):  
    i = index
    while i >= 0 and array[i] > value:
        array[i + 1] = array[i]
        i -= 1
    array[i + 1] = value

def insertion_sort(arr):
    array = arr[:]
    for i in range(0, len(array) - 1):
        insert(array, i, array[i + 1])
    return array

print("Insertion sort")
print(x)
print(insertion_sort(x))