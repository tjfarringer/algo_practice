

import time
from random import randint
import random

# merge sort key idea:
# step 1 - recursively sort 1st half
# step 2 - recursively sort 2nd half
# We need to split the lists until they have a single element
# A list with a single element is sorted
# traverse each step using pointers to merge the halves

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, 2]

for x in range(0, 100000):
    A.append(randint(-1000, 1000))



def partition(array: list):
    '''
    split the list into two blocks

    :param array:
    :param low:
    :param high:
    :return:
    '''

    midpoint = len(array) // 2
    return array[:midpoint], array[midpoint:]


def merge_two_sorted_lists(left_array: list, right_array: list):
    '''
    This takes to lists

    :param left_array:
    :param right_array:
    :return:
    '''
    # Special case: one or both of lists are empty
    if len(left_array) == 0:
        return right_array
    elif len(right_array) == 0:
        return left_array

    merged_array = []
    merged_array_length = len(left_array) + len(right_array)

    i = j = 0

    while len(merged_array) < merged_array_length:
        # if we are at the end of the left-array , simply add from the right-array
        if (i+1) > len(left_array) and (j+1) <= len(right_array):
            merged_array.append(right_array[j])
            j += 1

        # if we are at the end of the right-array , simply add from the left-array
        elif (i+1) <= len(left_array) and (j+1) > len(right_array):
            merged_array.append(left_array[i])
            i += 1


        elif (i+1) <= len(left_array) and left_array[i] <= right_array[j]:
            merged_array.append(left_array[i])
            i += 1


        elif (j+1) <= len(right_array) and left_array[i] > right_array[j]:
            merged_array.append(right_array[j])
            j += 1

    return merged_array
#

def merge_sort(array: list):
    '''
    take a list, sort it into two lists.  Sort each list and then combine the results.
    '''

    if len(array) <= 1:
        return array
    else:
        # split the lists
        left_array, right_array = partition(array)
        # combine the lists
        # note that we need to further break down the lists until they are composed of 1 element each
        merged_lists = merge_two_sorted_lists(merge_sort(left_array), merge_sort(right_array))

        return merged_lists


def main():
    start = time.time()
    merge_sort(A)
    end = time.time()
    print('time elapsed: ', end - start)


if __name__ == "__main__":
    main()





