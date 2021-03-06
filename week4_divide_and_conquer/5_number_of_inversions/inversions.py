#Problem Introduction#
#An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such that 𝑎𝑖 > 𝑎𝑗. The number of inversions of a sequence in some sense measures how close the sequence is to being sorted. For example, a sorted (in non-descending order) sequence contains no inversions at all, while in a sequence sorted in descending order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2 inversions).

#Problem Description#
#Task: The goal in this problem is to count the number of inversions of a given sequence.
#Input Format: The first line contains an integer 𝑛, the next one contains a sequence of integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
#Constraints: 1 ≤ 𝑛 ≤ 105, 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.
#Output Format: Output the number of inversions in the sequence.


import sys

def get_number_of_inversions(arr, temp_arr, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(arr, temp_arr, left, ave)
    number_of_inversions += get_number_of_inversions(arr, temp_arr, ave, right)
    number_of_inversions += merge_and_count(left, ave, right, arr, temp_arr)    
    return number_of_inversions
    
def merge_and_count(l, m, r, a, temp_a):
    i = l
    j = m
    k = l
    number_of_inversions = 0
    
    while (i < m) and (j < r):
        if a[i] <= a[j]:
            temp_a[k] = a[i]            
            i += 1
            k += 1
        
        if a[i] > a[j]:
            temp_a[k] = a[j]
            number_of_inversions += m - i
            j += 1
            k += 1
            
    while (i < m):
        temp_a[k] = a[i]            
        i += 1
        k += 1
            
    while (j < r):
        temp_a[k] = a[j]            
        j += 1
        k += 1

    k = l

    while (k < r):
        a[k] = temp_a[k]
        k += 1
    
    return number_of_inversions
    

if __name__ == '__main__':    
    n = int(input())
    arr = list(map(int, input().split()))
    temp_arr = n * [0]
    print(get_number_of_inversions(arr, temp_arr, 0, n))
