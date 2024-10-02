"""
## THIS IS THE GIVEN SAMPLE I/O FROM THE PROJECT RUBRIC

Welcome to the test suite of selected sorted algorithms!

Select the sorting algorithm you want to test.
-------------------------
1. Bubble Sort
2. Merge Sort
3. Quick Sort
4. Heap Sort (replacing this line with the algorithm you choose)
5. Exit
Select a sorting algorithm (1-5): 1
## notice here that the algorithm doesn't run until a case scenario is selected
Case Scenarios for Bubble Sort
----------------
1. Best Case
2. Average Case
3. Worst Case
4. Exit bubble sort test

Select the case (1-4): 1

In best case,
For N = 100,    it takes 0.000011 seconds
For N = 1000,   it takes 0.000056 seconds
For N = 10000,  it takes 0.000583 seconds
## n being our size
Do you want to input another N (Y/N)? Y
What is the N? 100000

For N = 100000, it takes 0.0090347 seconds.

Do you want to input another N (Y/N)? N
##  back a menu here to selections
Case Scenarios for Bubble Sort
----------------
1. Best Case
2. Average Case
3. Worst Case
4. Exit bubble sort test

Select the case (1-4): 4
## back to main menu
Select the sorting algorithm you want to test.
-------------------------
1. Bubble Sort
2. Merge Sort
3. Quick Sort
4. Heap Sort (replacing this line with the algorithm you choose)
5. Exit
Select a sorting algorithm (1-5): 5

Bye!



# Record time taken to sort data
start_time = time.time()
sort_function(sorted_data)
end_time = time.time()

"""
"""    
# average case
if complexity_selection == '2':
    #alskdjfhalskdjhf
    gen_data(size, complexity_selection)
# worse case
if complexity_selection == '3':
    #as;dflkasdf
    gen_data(size, complexity_selection)
# Exit program
if complexity_selection == '4':
    print("Exiting case selection.")
    print("")
    break

"""

import time
import random

TIM_MIN_RUN = 32
    
"""
    The main idea behind Tim Sort is to exploit the existing 
    order in the data to minimize the number of comparisons 
    and swaps. It achieves this by dividing the array into 
    small subarrays called runs, which are already sorted, 
    and then merging these runs using a modified merge sort 
    algorithm.
"""
# Calculates minimum run
def calculate_minRun(n):
    run = 0
    while n >= TIM_MIN_RUN:
        run |= n & 1 
        n >>= 1 
    return n + run


# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertion_sort(insArray, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and insArray[j] < insArray[j - 1]:
            insArray[j], insArray[j - 1] = insArray[j - 1], insArray[j]
            j -= 1

# Merge function merges the sorted runs
def tim_merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], [] 
    for i in range(0, len1): 
        left.append(arr[int(l + i)]) 
    for i in range(0, len2): 
        right.append(arr[int(m + 1 + i)]) 
  
    i, j, k = 0, 0, l
    
    # after comparing, we merge those two array 
    # in larger sub array 
    while i < len1 and j < len2: 
        if left[i] <= right[j]: 
            arr[k] = left[i] 
            i += 1
        else: 
            arr[k] = right[j] 
            j += 1
        k += 1
  
    # Copy remaining elements of left, if any 
    while i < len1: 
        arr[k] = left[i] 
        k += 1
        i += 1
  
    # Copy remaining element of right, if any 
    while j < len2: 
        arr[k] = right[j] 
        k += 1
        j += 1
    

def tim_sort(data): 
    start_time = time.time()
    n = len(data) 
    minRun = calculate_minRun(n) 
  
    # Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertion_sort(data, start, end) 
  
    # Start merging from size RUN (or 32 being the minimum). It will merge 
    # to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 
  
        # Pick starting point of left sub array,
        # merge arr[left..left + size - 1] and
        # arr[left + size, left + 2 * size -1] 
        # After every merge, we increase left by 2 * size 
        for left in range(0, n, 2 * size): 
  
            # Find ending point of left sub array 
            # mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
  
            # Merge sub array arr[left.....mid] & 
            # arr[mid + 1....right] 
            if mid < right: 
                tim_merge(data, left, mid, right) 
  
        size = 2 * size 
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken, data

def bubble_sort(data):
    # bubble sort loops through the list and pushes the biggest number to the top
    # it does this a number of times equal to the size of the list -1 
    sorted = False
    start_time = time.time()
    for i in range(len(data)-1):
        swap = False
        if not sorted:
            for j in range(len(data) - i - 1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    swap = True
            if not swap:
                sorted = True
                break
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken, data
    # Continue
    
def merge_sort(data):
    """ Enter function info """
    start_time = time.time()
    # Base case
    if len(data) <= 1:
        end_time = time.time()
        time_taken = end_time - start_time
        return time_taken, data

    # Check if data is already sorted
    if all(data[i] <= data[i+1] for i in range(len(data)-1)):
        end_time = time.time()
        time_taken = end_time - start_time
        return time_taken, data
    
    # Divide and recurse
    midIndex = len(data)//2
    leftHalf = data[:midIndex]
    rightHalf = data[midIndex:]
       
    leftHalf = merge_sort(leftHalf)
    rightHalf = merge_sort(rightHalf)

    # Skip merge if largest value in left half is <= smallest value in right
    if int(leftHalf[-1]) <= int(rightHalf[0]):
        end_time = time.time()
        time_taken = end_time - start_time
        return time_taken, leftHalf + rightHalf
    
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken, merge(leftHalf,rightHalf)

def merge(left, right):
    """merge function here"""
    result = []
    leftIndex, rightIndex = 0,0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    if rightIndex < len(right):
        result.extend(right[rightIndex:])
    return result

def quick_sort(data):
    #quick sort choses a pivot point then puts all smaller numbers to the left
    #and all larger numbers to the right. it recursively does this until every
    #number has been a pivot and the entire list in sorted
    
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    # Continue


     
"""
Suggestion from Jon - make gen_data its own function 
and run the sort inside of main on the generated data 
instead of inside of gen_data. Will make implementation
easier to do and follow.

Record the time taken to run the sort in the same function as
the sorting algorithm instead of a seperate func1tion

"""

# Generates data and runs sorting function
def gen_data(size, complexity_selection):
    """ Enter function info """
    if (complexity_selection == '1' or '2' or '3'):
        data = []
        if complexity_selection == '1': # Best case
            data = [i for i in range(size)]
        elif complexity_selection == '2': # Average case
            data = [random.randint(0,size) for x in range(size)]
        elif complexity_selection == '3': # Worst case
            data = [i for i in range(size, 0, -1)]
        else:
            raise ValueError("Invalid selection!")

    # Make a copy to avoid modifying original data
    data_to_sort = data.copy()
    return data_to_sort

def test_sorting_function(sort_function, data):
    """ Test the sorting function on a dataset of 10. """
    print("-" * 20)
    print(f"Testing {sort_function.__name__} on small dataset...")
    print("")
    
    # Print unsorted data
    print(f"Unsorted Data: {data}")
    print("")
    
    # Make a copy to avoid modifying original data
    sorted_data = data.copy()
    new_data = sort_function(sorted_data)
    
    print(f"Sorted Data: {new_data}")
    print("-" * 20)
    
# this is for debugging purposes only     
"""
     # Test sorting function on dataset of 10 numbers
     small_dataset = [random.randint(1,100) for x in range(10)]
     test_sorting_function(sorting_algorithms[sort_selection],
                           small_dataset)
"""
"""
    this is what will record the time taken to run the sorts and display information.
    we will be moving this into the sorting functions themselves rather than inside
    of the gen_data function.
    
    print(f"Running {sort_function.__name__} on data of size {size}...)")
    print("")
    
    
    
    # Display time taken to sort data
    print(f"{sort_function.__name__}: {end_time - start_time:.6f} seconds")
    print("")
    print("-" * 10)
    
"""   
    
def main():
    """ Main driver program. """
    # Welcome Menu
    print("Welcome to the test suite of selected sorting algorithms!")
    print("")
    
    # Place options into dictionaries
    sorting_algorithms = {
        '1' : bubble_sort,
        '2' : merge_sort,
        '3' : quick_sort,
        '4' : tim_sort,
        '5' : None
        }
    
    complexity_options = {
        '1' : 'Best Case',
        '2' : 'Average Case',
        '3' : 'Worst Case',
        '4' : 'Exit test'
        }
    
    while True:
        # Prompt user for sorting algorithm selection
        while True:
            print("Select the sorting algorithm you want to test.")
            print ("-" * 25)
            
            # Display sorting algorithms
            for key, sort_function in sorting_algorithms.items():
                if sort_function:
                    print(f"{key}. {sort_function.__name__}")
                else:
                    print(f"{key}. Exit")
            print("")
            
            sort_selection = input("Select a sorting algorithm (1-5): ")
            print("")
            
            if sort_selection in sorting_algorithms:
                # Exit program
                if sort_selection == '5':
                    print("Exiting program.")
                    print("")
                    return
                break
            else:
                print("Invalid selection!")
                print("")
         
        # for case selection, data must first be generated based upon the user's
        # case selection. Then the sorting algorithm ran on 100, 1000, and 10000.
        
    
        # Prompt user for case scenario selection
        while True:
            print(f"Case Scenarios for {sorting_algorithms[sort_selection].__name__}")
            print("-" * 15)
        
            # Display time complexity options
            for key, complexity in complexity_options.items():
                print(f"{key}. {complexity}")
            print("")    
            
            complexity_selection = input("Select the case (1-4): ")
            print("")
            
            # complexity options is another dictionary defined at top of main
            
            if complexity_selection == '4':
                break
            
            
            # bubble_sort
            # merge_sort
            # quick_sort
            # case complexity selection from user
            if complexity_selection == '1' or '2' or '3':
                # this is a test
                unsorted_data = gen_data(100, complexity_selection)
                time_to_display, sorted_data = ((sorting_algorithms[sort_selection])(unsorted_data))
                # time_to_display, sorted_data = bubble_sort(unsorted_data)
                print(f"For N = 100,     it takes {time_to_display:.6f} seconds")
                
                unsorted_data = []
                unsorted_data = gen_data(1000, complexity_selection)
                # menu broken because of timers, will implement timers inside of main here, before and after
                # the sorting algorithms are called. 
                time_to_display, sorted_data = ((sorting_algorithms[sort_selection])(unsorted_data))
                
                print(f"For N = 1000,    it takes {time_to_display:.6f} seconds")
                
                unsorted_data = []
                unsorted_data = gen_data(10000, complexity_selection)
                time_to_display, sorted_data = ((sorting_algorithms[sort_selection])(unsorted_data))
                print(f"For N = 10000,   it takes {time_to_display:.6f} seconds")
                print("")
                
                yes_no = input("Do you want to input another N (Y/N)? ")
                
                if (yes_no == "N"):
                    break
                
                # there was an if statement here instead of a while, making the menu not loop
                # back like it was supposed to after selecting Y / N
                while (yes_no == "Y"):
                    new_Size = int(input("What is the N? "))
                    print("")
                    unsorted_data = []
                    unsorted_data = gen_data(new_Size, complexity_selection)
                    time_to_display, sorted_data = ((sorting_algorithms[sort_selection])(unsorted_data))
                    print(f"For N = {new_Size}, it takes {time_to_display:.6f} seconds")
                    print("")
                    
                    yes_no = input("Do you want to input another N (Y/N)? ")
                
            elif complexity_selection == '4':
                print("Exiting case selection.")
                print("")
                break
            
            else:
                print("Invalid selection!")
                print("")
           
main()



