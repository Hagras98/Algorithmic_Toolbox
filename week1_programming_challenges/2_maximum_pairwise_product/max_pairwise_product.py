def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1 = numbers[0]
    max2 = numbers[1]
    if n>2:
        for number in numbers[2:]:
            if number > max1:        
                if max1 > max2:
                    max2 = max1
                max1 = number
            elif number > max2:
                max2 = number
    max_product = max1 * max2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
