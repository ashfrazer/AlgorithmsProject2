import time
import random

def bubble_sort(data):
    """ Enter function info """
    print("Bubble sort is running...")
    print("")
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
        
    # Make a copy to avoid modifying original data
    sorted_data = data.copy()

    print(f"Running {sort_function.__name__} on data of size {size}...)")
    print("")

    # Record time taken to sort data
    start_time = time.time()
    sort_function(sorted_data)
    end_time = time.time()
    
    # Display time taken to sort data
    print(f"{sort_function.__name__}: {end_time - start_time:.4f} seconds")
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
    sort_function(sorted_data)
    
    print(f"Sorted Data: {sorted_data}")
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