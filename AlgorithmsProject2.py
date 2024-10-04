import time
import random

def calculate_min_run(n):
    """
    (Helper function for tim_sort)
    Calculates minimum run for TimSort
    Args:
        n : Number of elements to be sorted.
    Returns:
        n + run : Minimum run size that determines the size of the runs to be used in tim_sort.
    """
    run = 0
    tim_min_run = 32
    while n >= tim_min_run:
        run |= n & 1
        n >>= 1
    return n + run

def insertion_sort(data, left, right):
    """
    (Helper function for tim_sort)
    Sorts portion of the array using insertion sort algorithm.
    Args:
        data: The list of elements to be sorted.
        left: The starting index of the portion to be sorted.
        right: The ending index of the portion to be sorted.
    Returns:
        None
    """
    for i in range(left + 1, right + 1):
        j = i
        while j > left and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1

def tim_merge(data, l, m, r):
    """
    (Helper function for tim_sort)
    Merges two sorted sublists of data.
    Args:
        data: The list of elements containing the sublists to be merged.
        l: The starting index of the sublist to be merged.
        m: The ending index of the first sorted sublist.
        r: The ending index of the second sorted array.
    Returns:
        None
    """
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(data[int(l + i)])
    for i in range(0, len2):
        right.append(data[int(m + 1 + i)])

    i, j, k = 0, 0, l

    # Merge two lists into larger sublist
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        data[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        data[k] = right[j]
        k += 1
        j += 1

def tim_sort(data):
    """
    Sorts a list using the TimSort algorithm, a hybrid sorting algorithm derived from 
    a combination of merge_sort and insertion sort.
    Args:
        data: The list of elements to be sorted.
    Returns:
        data: The sorted list of elements (modified).
    """
    n = len(data)
    min_run = calculate_min_run(n)

    # Sort individual sublists of size RUN
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(data, start, end)

    # Start merging from size RUN (min 32), then 64, 128, 256, etc.
    size = min_run
    while size < n:
        # Merge data[left...left + size - 1] with data[left + size...left + 2 * size - 1]
        # Increment left by 2 * size after each merge
        for left in range(0, n, 2 * size):
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            # Merge sub array arr[left.....mid] & arr[mid + 1....right]
            if mid < right:
                tim_merge(data, left, mid, right)
        size *= 2
    return data

def bubble_sort(data):
    """
    Sorts a list using bubble sort algorithm.
    Args:
        data: The list of elements to be sorted.
    Returns:
        data: The sorted list of elements (modified).
    """
    n = len(data)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break
    return data

def merge_sort(data):
    """
    Sorts a list using the merge sort algorithm.
    Args:
        data: The list of elements to be sorted.
    Returns:
        data: The sorted list of elements (modified).
    """
    # Base case
    if len(data) <= 1:
        return data

    # Divide and recurse
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def merge(left, right):
    """
    (Helper function for merge_sort)
    Merges two sorted lists into a single sorted list.
    Args:
        left: A sorted list of elements to be merged.
        right: A sorted list of elements to be merged.
    Returns:
        result: A sorted list of elements from 'left' and 'right'.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def median_of_three(data, low, high):
    """
    Finds the median of the first, middle, and last elements of a list.
    Args:
        data: The list of elements to be sorted. The median is calculated from this list.
        low: The starting index of the sublist.
        high: The ending index of the sublist.
    Returns:
        mid: The index of the median value of the three elements.
    """
    mid = (low + high) // 2
    # Sort elements and use median as pivot
    if data[low] > data[mid]:
        data[low], data[mid] = data[mid], data[low]
    if data[low] > data[high]:
        data[low], data[high] = data[high], data[low]
    if data[mid] > data[high]:
        data[mid], data[high] = data[high], data[mid]
    return mid

def quick_sort(data, low=0, high=None):
    """
    Sorts a list using the quick sort algorithm.
    Args:
        data: The list of elements to be sorted.
        low: The starting index of the sublist. Defaults to 0.
        high: The ending index of the sublist. Defaults to None.
    Returns:
        None
    """
    if high is None:
        high = len(data) - 1
    if low < high:
        # Use median-of-three to find the pivot
        pivot_index = median_of_three(data, low, high)
        data[pivot_index], data[high] = data[high], data[pivot_index]  # Move pivot to end
        pivot_new_index = partition(data, low, high)
        quick_sort(data, low, pivot_new_index - 1)  # Sort left part
        quick_sort(data, pivot_new_index + 1, high)  # Sort right part

def partition(data, low, high):
    """
    Partitions the sublist of a list around a pivot.
    Args:
        data: The list of elements to be partitioned.
        low: The starting index of the sublist.
        high: The ending index of the sublist.
    Returns:
        i + 1: The index of the pivot.
    """
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

def gen_data(size, case_type):
    """
    Generates list of integers based on chosen time complexity type.
    Args:
        size: The number of elements to be generated.
        case_type: The chosen time complexity case to generate.
    Returns:
        data: A list of integers.
    """
    if case_type == '1':  # Best case: generates data in ascending order
        return [i for i in range(size)]
    elif case_type == '2':  # Average case: generates randomized data
        return [random.randint(0, size) for i in range(size)]
    elif case_type == '3':  # Worst case: generates data in descending order
        return [i for i in range(size, 0, -1)]
    else:
        raise ValueError("Invalid case type!")

def measure_sort_time(sort_function, data):
    """
    Measures the time taken to execute a sorting function.
    Args:
        sort_function: The sorting function to be called.
        data: The list of elements to be sorted.
    Returns:
        total_time: The total time taken to execute the sorting function (seconds).
    """
    start_time = time.perf_counter()  # start timer
    sort_function(data)
    end_time = time.perf_counter()  # end timer
    total_time = end_time - start_time # total time
    return total_time

def main():
    """
    Main Driver function.
    Args:
        None
    Returns:
        None
    """
    print("Welcome to the test suite of selected sorting algorithms!\n")

    # Place sorting algorithms into dictionary
    sorting_algorithms = {
        '1': bubble_sort,
        '2': merge_sort,
        '3': quick_sort,
        '4': tim_sort,
        '5': None
    }

    # Place time complexities into dictionary
    complexity_options = {
        '1': 'Best Case',
        '2': 'Average Case',
        '3': 'Worst Case',
        '4': 'Exit'
    }

    while True:
        # Prompt user for sorting algorithm selection
        print("Select the sorting algorithm you want to test.")
        print("-" * 15)
        for key, func in sorting_algorithms.items():
            if func:
                print(f"{key}. {func.__name__}")
            else:
                print(f"{key}. Exit")
        sort_choice = input("Select a sorting algorithm (1-5): ")
        if sort_choice not in sorting_algorithms:
            print("Invalid selection!")
            continue
        if sort_choice == '5':
            print("Exiting program.\n")
            break

        # Prompt user for case scenario selection
        while True:
            print(f"\nCase Scenarios for {sorting_algorithms[sort_choice].__name__}")
            print("-" * 15)
            for key, complexity in complexity_options.items():
                if complexity != 'Exit': 
                    print(f"{key}. {complexity}")
                else:
                    print(f"{key}. Exit {sorting_algorithms[sort_choice].__name__} test")
            print("")
            complexity_selection = input("Select the case (1-4): ")
            print("")
            if complexity_selection not in complexity_options:
                print("Invalid selection!")
                continue
            if complexity_selection == '4':
                break

            # Run sorting algorithm under specified time complexity
            sizes = [100, 1000, 10000]
            print(f"In {complexity_options[complexity_selection]},")
            for size in sizes:
                # Generate data
                data = gen_data(size, complexity_selection)
                # Measure time taken to sort
                time_taken = measure_sort_time(sorting_algorithms[sort_choice], data.copy())
                print(f"For N = {size}, it takes {time_taken:.6f} seconds.")
            print("")
            # Prompt user for another size
            while True:
                new_size = input("Do you want to input another N (Y/N)? ").lower()
                if new_size == 'y':
                    custom_size = int(input("What is the N? "))
                    print("")
                    data = gen_data(custom_size, complexity_selection)
                    time_taken = measure_sort_time(sorting_algorithms[sort_choice], data.copy())
                    print(f"For N = {custom_size}, it takes {time_taken:.6f} seconds.\n")
                else:
                    break

main()