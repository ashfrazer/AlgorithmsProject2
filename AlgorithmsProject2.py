import time
import random

def bubble_sort(data):
    """ Enter function info """
    print("Bubble sort is running...")
    # Continue
    
def merge_sort(data):
    """ Enter function info """
    print("Merge sort is running...")
    print("")
    # Continue

def quick_sort(data):
    """ Enter function info """
    print("Quick sort is running...")
    print("")
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
        
    # Make a copy of the data so that original date is not modified by
    #   sorting algorithms
    unsorted_data = data.copy()

    print(f"Running {sort_function.__name__} on data of size {size}...)")
    print("")

    # Record time taken to sort data
    start_time = time.time()
    sort_function(unsorted_data) # Sorting the UNSORTED data (copy)
    end_time = time.time()
    
    # Display time taken to sort data
    print(f"{sort_function.__name__}: {end_time - start_time:.4f} seconds")
    print("")
    print("-" * 10)

def main():
    """ Enter function info """
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
        '4' : 'Exit quick sort test'
        }
    
    while True:
        # Prompt user for sorting algorithm selection
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
        
        # Exit program
        if sort_selection == '5':
            print("Exiting program.")
            print("")
            break
        
        if sort_selection not in sorting_algorithms:
            raise ValueError("Invalid selection!")
    
        # Prompt user for case scenario selection
        print(f"Case Scenarios for {sorting_algorithms[sort_selection].__name__}")
        print("-" * 15)
    
        # Display time complexity options
        for key, complexity in complexity_options.items():
            print(f"{key}. {complexity}")
        print("")    
        
        complexity_selection = input("Select the case (1-4): ")
    
        # Exit program
        if complexity_selection == '4':
            print("Exiting case selection.")
            print("")
            continue
            
        if complexity_selection not in complexity_options:
            raise ValueError("Invalid selection!")
            print("")
        
        # Sort data in sets of 100, 1000, 10000, and 100000
        for size in [100, 1000, 10000, 100000]:
            gen_data(sorting_algorithms[sort_selection], size,
                     complexity_selection)
    
main()