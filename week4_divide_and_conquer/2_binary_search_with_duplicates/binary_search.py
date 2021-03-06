#Problem Description#
#Task: Find the first occurence of an integer in the given sorted sequence of integers (possibly with duplicates).
#Input Format: The first two lines of the input contain an integer ๐ and a sequence ๐0 โค ๐1 โค ยท ยท ยท โค ๐๐โ1 of ๐ positive integers in non-decreasing order. The next two lines contain an integer ๐ and ๐ positive integers ๐0, ๐1, . . . , ๐๐โ1.
#Constraints: 1 โค ๐ โค 105; 1 โค ๐ โค 3 ยท 104; 1 โค ๐๐ โค 109 for all 0 โค ๐ < ๐; 1 โค ๐๐ โค 109 for all 0 โค ๐ < ๐;
#Output Format: For all ๐ from 0 to ๐ โ 1, output an index 0 โค ๐ โค ๐ โ 1 of the first occurrence of ๐๐ (i.e., ๐๐ = ๐๐) or โ1 if there is no such index.


def binary_search_first_instance(keys, query):
    low = 0
    high = len(keys)-1
    mid = low+((high-low)//2)
    while low <= high:
        if (query == keys[mid]) and (mid == 0 or query > keys[mid - 1]):
            return mid
        if query > keys[mid]:
            low = mid + 1
            mid = low + ((high-low)//2)
        else:
            high = mid - 1
            mid = low + ((high-low)//2)
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_first_instance(input_keys, q), end=' ')
