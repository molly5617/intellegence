# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:25:09 2022

@author: jerem
"""

def search(n, arr):
    arr.sort()
    front = 0
    end = len(arr)-1
    while end > front:
        middle = (front + end) // 2
        if n == arr[middle]:
            while n == arr[middle]:
                middle -= 1
            return middle+1
        elif n > arr[middle]:
            front = middle + 1
        else:
            end = middle - 1
    if arr[end] > n: return end
    else: return end+1
            
def adjust(i, n):
    chd = 2 * i #兒子
    itemx = x[i-1] #被選中的值   
    itemy = y[i-1] #被選中的值
    
    # 代表兒子存在
    while chd <= n:
        # 代表右兒子存在，且右兒子>左兒子
        if chd < n and x[chd-1] < x[chd]: 
            # 選擇右兒子作為兒子
            chd += 1
        
        # 若父值>=子值 跳出迴圈
        if itemx >= x[chd-1]:
            break
            
        # 否則將父值填入兒子
        y[(chd // 2)-1] = y[chd-1]
        x[(chd // 2)-1] = x[chd-1]
        
        chd *= 2
    
    y[int(chd // 2)-1] = itemy
    x[int(chd // 2)-1] = itemx
    
def heapify(n):
    for i in range(int(n // 2), 0, -1):
        adjust(i, len(x))
        
def heapSort(n):
    heapify(len(x))
    for i in range(n, 1, -1):
        y[i-1], y[0] = y[0], y[i-1]
        x[i-1], x[0] = x[0], x[i-1]
        adjust(1, i-1)

def rank(start, end):
    if end - start == 1:
        if y[end] > y[start]: r[end] += 1
        return
    if end - start == 0:
        return
    
    median = (start+end)//2
    rank(start, median-1)
    rank(median, end)
    
    for i in range(median, end+1, 1):
        v = search(y[i], y[start: median])
        if v > 0:
            r[i] += v
    
    

file = open("test2.txt")
data_str = file.read()
file.close()
data = data_str.split('\n')

y = []
x = []
r = []
for i in data:
    t = i.split(" ")
    x.append(float(t[0]))
    y.append(float(t[1]))
    r.append(0)

heapSort(len(x))
rank(0, len(x)-1)
maxrank = max(r)
minrank = min(r)
totalrank = 0
for i in r:
    totalrank += i
avgrank = totalrank / len(x)


for i in range(len(x)):
    print('(', end = "")
    print(x[i], end = "")
    print(', ', end = "")
    print(y[i], end = "")
    print(") rank = ", end = '')
    print(r[i])
print()
print('檔案中所有點的個數: ', end='')
print(len(x))
    
print('最大rank: ', end='')
print(maxrank)

print('最小rank: ', end='')
print(minrank)

print('平均rank: ', end='')
print(round(avgrank, 2))