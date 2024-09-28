import time
import random

def bubble_sort(data):
    # bubble sort loops through the list and pushes the biggest number to the top
    # it does this a number of times equal to the size of the list -1 
    sorted = False
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
    return data
    # Continue
    
def merge_sort(data):
    """ Enter function info """

    # Base case
    if len(data) <= 1:
        return data

    # Check if data is already sorted
    if all(data[i] <= data[i+1] for i in range(len(data)-1)):
        return data
    
    # Divide and recurse
    midIndex = len(data)//2
    leftHalf = data[:midIndex]
    rightHalf = data[midIndex:]
       
    leftHalf = merge_sort(leftHalf)
    rightHalf = merge_sort(rightHalf)

    # Skip merge if largest value in left half is <= smallest value in right
    if leftHalf[-1] <= rightHalf[0]:
        return leftHalf + rightHalf

    return merge(leftHalf,rightHalf)

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
    #number has been a pivot and the entier list in sorted
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    # Continue

def tim_sort(data):
    """ Enter function info """
    print("Tim sort is running...")
    print("")
    # Continue
     
# Generates data and runs sorting function
def gen_data(sort_function, size, complexity_selection):
    """ Enter function info """
    if complexity_selection == '1': # Best case
        data = [i for i in range(size)]
    elif complexity_selection == '2': # Average case
        data = [random.randint(0,size) for x in range(size)]
    elif complexity_selection == '3': # Worst case
        data = [i for i in range(size, 0, -1)]
    else:
        raise ValueError("Invalid selection!")
        
    # Make a copy to avoid modifying original data
    sorted_data = data.copy()

    print(f"Running {sort_function.__name__} on data of size {size}...)")
    print("")

    # Record time taken to sort data
    start_time = time.time()
    sort_function(sorted_data)
    end_time = time.time()
    
    # Display time taken to sort data
    print(f"{sort_function.__name__}: {end_time - start_time:.6f} seconds")
    print("")
    print("-" * 10)

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
    
        # Test sorting function on dataset of 10 numbers
        small_dataset = [random.randint(1,100) for x in range(10)]
        test_sorting_function(sorting_algorithms[sort_selection],
                              small_dataset)
    
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
        
            # Exit program
            if complexity_selection == '4':
                print("Exiting case selection.")
                print("")
                break
            elif complexity_selection in complexity_options:
                # Sort data in sets of 100, 1000, 10000, and 100000
                for size in [100, 1000, 10000, 100000]:
                    gen_data(sorting_algorithms[sort_selection], size,
                             complexity_selection)
                break
            else:
                print("Invalid selection!")
                print("")
         
main()