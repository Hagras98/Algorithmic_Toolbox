#Problem Introduction#
#In this problem, you will implement the binary search algorithm that allows searching very efficiently (even huge) lists, provided that the list is sorted.

#Problem Description#
#Task: The goal in this code problem is to implement the binary search algorithm.
#Input Format: The first two lines of the input contain an integer ๐ and a sequence ๐0 < ๐1 < ยท ยท ยท < ๐๐โ1 of ๐ distinct positive integers in increasing order. The next two line contain an integer ๐ and ๐ positive integers ๐0, ๐1, . . . , ๐๐โ1.
#Constraints: 1 โค ๐ โค 105; 1 โค ๐ โค 3 ยท 104; 1 โค ๐๐ โค 109 for all 0 โค ๐ < ๐; 1 โค ๐๐ โค 109 for all 0 โค ๐ < ๐;
#Output Format: For all ๐ from 0 to ๐ โ 1, output an index 0 โค ๐ โค ๐ โ 1 such that ๐๐ = ๐๐ or โ1 if there is no such index.


def binary_search(keys, query):
    low = 0
    high = len(keys)-1
    mid = int(low+((high-low)/2))
    while low <= high:
        if query == keys[mid]:
            return mid
        elif query > keys[mid]:
            low = mid + 1
            mid = int(low + ((high-low)/2))
        elif query < keys[mid]:
            high = mid - 1
            mid = int(low + ((high-low)/2))
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
