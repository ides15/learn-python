from timeit import default_timer

def mergeSort(array):
    # base case, if array length is 1 or 0, return the given array
    if len(array) > 1:
        # splits the array up into 2 parts
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        # calling mergeSort on each side of the array recursively
        mergeSort(left)
        mergeSort(right)

        leftIndex = rightIndex = finalIndex = 0
        # compare each side of the array and input the lower number of the index into the final arr
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                array[finalIndex] = left[leftIndex]
                leftIndex += 1
            else:
                array[finalIndex] = right[rightIndex]
                rightIndex += 1
            finalIndex += 1

        # clean up the rest of the left side of the array (if it isn't fully iterated)
        while leftIndex < len(left):
            array[finalIndex] = left[leftIndex]
            leftIndex += 1
            finalIndex += 1

        # clean up the rest of the right side of the array (if it isn't fully iterated)
        while rightIndex < len(right):
            array[finalIndex] = right[rightIndex]
            rightIndex += 1
            finalIndex += 1

    return array

starttime = default_timer()
print(mergeSort([5, 4, 1, 3, 2]))
endtime = default_timer()
print('Merge sort: ', str(endtime - starttime))

print()

starttime = default_timer()
print(sorted([5, 4, 1, 3, 2]))
endtime = default_timer()
print('Default sort: ', str(endtime - starttime))
