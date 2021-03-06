#Problem Introduction#
#Majority rule is a decision rule that selects the alternative which has a majority, that is, more than half the votes. Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, you would like to check whether it contains an element that appears more than 𝑛/2 times. 

#Problem Description#
#Task: The goal in this code problem is to check whether an input sequence contains a majority element.
#Input Format: The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
#Constraints: 1 ≤ 𝑛 ≤ 105; 0 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.
#Output Format: Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, and 0 otherwise.


def binary_search_first_instance(keys, query):
    low = 0
    high = len(keys)-1
    mid = low+((high-low)//2)
    while low <= high:
        if (query == keys[mid]) and (mid == 0 or query > keys[mid-1]):
            return mid
        if query > keys[mid]:
            low = mid + 1
            mid = low+((high-low)//2)
        else:
            high = mid - 1
            mid = low+((high-low)//2)       
    return -1

def get_majority_element(a, left, right):     
    a.sort()
    mid = (right - left) // 2 + left        
    first =  binary_search_first_instance(a, a[mid])      
    try:
        if a[first] == a[mid + first]:
            return mid
        else: 
            return -1
    except:
        return -1
    
    

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
