"""
sum the differences between consecutive
pairs in the array in descending order.
"""


def sum_of_differences(arr):
    num_sum = 0
    arr.sort(reverse=True)
    if len(arr) <= 1:
        return 0
    else:
        for index in range(len(arr)):
            if arr[index] == arr[-1]:
                continue
            else:
                num_sum += arr[index] - arr[index + 1]
    return num_sum


array = [-1]
print(sum_of_differences(array))
