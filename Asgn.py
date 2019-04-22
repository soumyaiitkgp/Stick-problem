# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:00:57 2019

@author: Soumya Yadav
"""

N = input("Please enter the number of sticks: ")

a = [int(i) for i in input("Enter the " + N + " numbers at the top end of the sticks with space: " ).split()]
b = [int(i) for i in input("Enter the " + N + " numbers at the bottom end of the sticks with space: " ).split()]
    
i = 0
x = 0
y = 0
z = 0
m = 0
n = 0

for i in range(len(a)):
    if a[i]%2 == 1:
        m = 1
        x = x+1
    else:
        m = 0
    if b[i]%2 == 1:
        n = 1
        y = y+1
    else:
        n = 0
    if m and n == 1:
        z = z+1

x = x-z
y = y-z
     
if z%2 == 1:
    if x%2 == 1 and y%2 == 1:
        print("Output is 0")
    if x ==0 and y ==0:
        print("Output is -1")
    else: 
        if x%2 == 0 and y%2 ==0:
            print("Output is 1")
    
if z%2 == 0:
    if x%2 == 1 and y%2 == 1:
        print("Output is 1")
    if x%2 == 0 and y%2 == 0:
        print("Output is 0")

#for odd numbers do not exist in pairs
if x%2 ==1 and y%2 ==0:
    print("Output is -1")
    
#for odd numbers do not exist in pairs
if x%2 ==0 and y%2 ==1:
    print("Output is -1")

   
    
    
    

 
