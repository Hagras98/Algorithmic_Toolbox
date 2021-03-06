#Problem Introduction#
#The goal in this problem is to redesign a given implementation of the randomized quick sort algorithm so that it works fast even on sequences containing many equal elements.

#Problem Description#
#Task: To force the given implementation of the quick sort algorithm to efficiently process sequences with few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.
#Input Format: The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛 integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
#Constraints: 1 ≤ 𝑛 ≤ 105; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.
#Output Format: Output this sequence sorted in non-decreasing order

import random

def partition3(a, l, r):
    pivot = a[l]
    j_low = l
    j_high = j_low 
    
    for i in range(l + 1, r + 1):
        if a[i] < pivot:
            j_low += 1
            j_high += 1
            if j_high < i:
                a[j_low], a[j_high] = a[j_high], a[j_low]
            a[i], a[j_low] = a[j_low], a[i]
        elif a[i] == pivot:
            j_high += 1
            a[i], a[j_high] = a[j_high], a[i]                        
    a[l], a[j_low] = a[j_low], a[l]    
    return [j_low, j_high]
    
    

def partition2(a, l, r):
    pivot = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1);
    randomized_quick_sort(a, m[1] + 1, r);


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
