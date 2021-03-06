#Problem Introduction#
#You are going to travel to another city that is located π miles away from your home city. Your car can travel at most π miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2, . . . , stopπ from your home city. What is the minimum number of refills needed?

#Problem Description#
#Input Format: The first line contains an integer π. The second line contains an integer π. The third line specifies an integer π. Finally, the last line contains integers stop1, stop2, . . . , stopπ.
#Output Format: Assuming that the distance between the cities is π miles, a car can travel at most π miles on a full tank, and there are gas stations at distances stop1, stop2, . . . , stopπ along the way, output the minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to reach the destination, output β1.
#Constraints: 1 β€ π β€ 105. 1 β€ π β€ 400. 1 β€ π β€ 300. 0 < stop1 < stop2 < Β· Β· Β· < stopπ < π.




# python3
import sys


def compute_min_refills(distance, tank, stops):
    full = tank
    refills = 0
    distance_covered = 0
    stops.append(distance) 
    for stop in stops:
        stop -= distance_covered
        if stop <= tank:
            tank -= stop
            distance_covered += stop
            continue
        elif stop > tank:
            if stop <= full:
                tank = full
                tank -= stop
                refills += 1
                distance_covered += stop
                continue
            elif stop > full:
                return -1
    return refills

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))

