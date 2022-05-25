def move_zeros(array):
    for i in range(len(array)):
        if array[i] == 0:
            array.remove(array[i])
            array.append(0)
    return array


array = [1, 0, 1, 2, 0, 1, 3]

print(move_zeros(array))
