


import time
from random import randint
import random

# quicksort key idea:  partition the array around a pivot element
# step 1 - pick pivot element
# step 2 - rearrange array so that:
# step 2a - left side of pivot is less than the pivot element
# step 2b - right side of pivot is greater than the pivot element
# run time is O(n)

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, 2]

for x in range(0, 1000000):
    A.append(randint(-10000, 10000))



def partition(array, low, high):
    '''

    :param array:  Array to sort
    :return:
    '''

    # choose pivot
    # this should be done randomly to improve speed
    p = random.choice(array[low:high+1])
    ## p = array[low]
    i = low + 1

    for j in range(low, high):
        if array[j] < p:
            print('i is: ', i, ' j is: ', j)
            array[i], array[j] = array[j], array[i]
            i += 1

    array[low], array[i-1] = array[i-1], array[low]

    return (i-1)

def three_way_partition(array, p, low, high):
    l = low
    r = low
    u = high

    while r <= u:
        if array[r] < p:
            array[l], array[r] = array[r], array[l]
            l += 1
            r += 1
        elif array[r] > p:
            array[u], array[r] = array[r], array[u]
            u += 1
        else: ## the element is equal to pivot
            r += 1
    return l, r

def quick_sort(array, low, high):
    '''

    :param array:
    :return:
    '''

    if len(array[low:high]) <= 1:
        return array

    if low < high:
        # find the pivot value
        p = partition(array, low, high)
        print('p is: ', p, ' low is: ', low, ' high is: ', high)
        # in case there are duplicates, we need to find left and right
        left, right = three_way_partition(array, p, low, high)

        # partition the first half
        quick_sort(array, low, left - 1)
        # partition the second half
        quick_sort(array, right, high)


def main():
    start = time.time()
    quick_sort(A, 0, len(A))
    end = time.time()
    print('time elapsed: ', end - start)


if __name__ == "__main__":
    main()
