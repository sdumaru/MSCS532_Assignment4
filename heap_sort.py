""" Understanding Heap Sort """

import timeit
import random
from memory_profiler import profile

def max_heapify(array, heap_size, index):
    """ Function to heapify a subtree rooted with node index """
    left = 2 * index + 1                        # Left child index with parent index
    right = 2 * index + 2                       # Right child index with parent index

    # Check to see if the left child of root exists and if it does,
    # check to see if the value is greater than the root.
    # Set the largest to the largest value index between left child and root
    if (left < heap_size) and (array[left] > array[index]):
        largest = left
    else:
        largest = index

    # Check to see if the right child of root exists and if it does,
    # check to see if the value is greater than the root.
    # Set the largest to the right child index in order to swap
    if (right < heap_size) and (array[right] > array[largest]):
        largest = right

    # If the largest is either left or right child, swap it with the root
    if largest is not index:
        array[index], array[largest] = array[largest], array[index]

        # Recursively heapify the affected subtree
        max_heapify(array, heap_size, largest)

def build_max_heap(array, array_size):
    """ Function to build a max heap from the array """
    # Since last parent will be at (array_size//2) it's the start point.
    for index in range(array_size // 2, -1, -1):
        max_heapify(array, array_size, index)

# @profile
def max_heap_sort(array):
    """ Function to sort the array using max heap """
    array_size = len(array)
    build_max_heap(array, array_size)

    # Extract the largest number one by one from the heap
    for index in range(array_size - 1, 0, -1):
        # The largest value element will go at the end of array and
        # heapify will be done with rest of the elements excluding last one
        array[index], array[0] = array[0], array[index]
        max_heapify(array, index, 0)

    return array

def print_execution_times(array_name):
    """ Function to print execution times """
    timer_stmt = '''max_heap_sort({0})'''
    times = timeit.repeat(stmt=timer_stmt.format(array_name), repeat=5, number=10000, globals=globals())
    print('total execution time: ' + str(min(times)))

def huge_random_array():
    """ Function to return huge number of random integers for testing purpose """
    array = []
    max_numbers = 500
    for i in range(max_numbers):
        array.append(random.randint(0, max_numbers))
    return array

# Testing performance of algorithms on these arrays
randomized_array = [23, 65, 98, 1, 36, 47, 76, 28, 83, 15]
sorted_array = [1, 15, 23, 28, 36, 47, 65, 76, 83, 98]
reversed_sorted_array = [98, 83, 76, 65, 47, 36, 28, 23, 15, 1]

# Print execution times for the array
print("RANDOM ARRAY", end = " ")
print_execution_times(randomized_array)

print("SORTED ARRAY", end = " ")
print_execution_times(sorted_array)

print("REVERSED SORTED ARRAY", end = " ")
print_execution_times(reversed_sorted_array)

print("HUGE RANDOM ARRAY", end = " ")
print_execution_times(huge_random_array())
