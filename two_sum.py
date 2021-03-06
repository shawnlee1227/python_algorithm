def find_two_sum_loops(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return (i, j)
    return None

def find_two_sum_map(numbers, target_sum):
    map = {} # val : index
    for i, n in enumerate(numbers):
        diff = target_sum - n
        if diff in map:
            return (map[diff], i)
        map[n] = i
    return None


if __name__ == "__main__":
    print(find_two_sum_loops([3, 1, 5, 7, 5, 9], 10))
    print(find_two_sum_map([5, 2, 6, 7, 1, 3], 10))