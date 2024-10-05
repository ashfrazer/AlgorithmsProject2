import matplotlib.pyplot as plt

# ADJUST AS NEEDED! Some sorting algorithms have different sizes due to performance!
# Bubble sort sizes: sizes = [10, 100, 1000, 10000, 50000]
# Merge sort sizes: sizes = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000, 2500000, 5000000]
# Quicksort sizes: sizes = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000, 2500000, 5000000]
# Quicksort SLOWER sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
# Tim sort sizes: sizes = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000, 2500000, 5000000]

sizes = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000, 2500000, 5000000]

bubble_sort_best = [
    0.000005,
    0.000004,
    0.000034,
    0.000381,
    0.001829
]

bubble_sort_average = [
    0.000008,
    0.000226,
    0.030650,
    3.366368,
    88.577238
]

bubble_sort_worst = [
    0.000009,
    0.000300,
    0.034943,
    4.172379,
    106.574532
]

merge_sort_best = [
    0.000016,
    0.000073,
    0.000770,
    0.009281,
    0.063901,
    0.108777,
    0.615068,
    1.330568,
    3.402204,
    7.230298
]

merge_sort_average = [
    0.000017,
    0.000097,
    0.001121,
    0.015084,
    0.088130,
    0.197607,
    1.118843,
    2.610186,
    6.733291,
    14.851445
]

merge_sort_worst = [
    0.000017,
    0.000082,
    0.000766,
    0.009440,
    0.053158,
    0.113837,
    0.651749,
    1.353201,
    3.723963,
    7.886171
]

quick_sort_best = [
    0.000014,
    0.000047,
    0.000519,
    0.006938,
    0.042152,
    0.088665,
    0.448490,
    0.954338,
    2.570784,
    5.483622
]

quick_sort_average = [
    0.000014,
    0.000053,
    0.000687,
    0.008985,
    0.054509,
    0.111835,
    0.688452,
    1.610836,
    4.289516,
    10.098525
]

quick_sort_worst = [
    0.000012,
    0.000053,
    0.000811,
    0.011659,
    0.076805,
    0.152445,
    1.012441,
    1.824682,
    5.017497,
    10.951906
]

quick_sort_slow = [
    0.000007,
    0.000211,
    0.000752,
    0.002819,
    0.006927,
    0.012631,
    0.015861,
    0.018184
]

tim_sort_best = [
    0.000008,
    0.000025,
    0.000307,
    0.004978,
    0.031684,
    0.069296,
    0.423105,
    0.919991,
    2.633415,
    5.173128
]

tim_sort_average = [
    0.000013,
    0.000068,
    0.001122,
    0.014072,
    0.089618,
    0.198958,
    1.169281,
    2.464795,
    6.698233,
    14.608754
]

tim_sort_worst = [
    0.000014,
    0.000093,
    0.001490,
    0.012896,
    0.090328,
    0.182198,
    1.141539,
    2.183705,
    4.872720,
    9.699101
]


def create_plot(sizes, best, average, worst, sorting_algorithm):
    plt.figure(figsize=(10, 6))

    # plotting (no markers)
    plt.plot(sizes, best, label=f"{sorting_algorithm} - Best Case", linestyle='-')
    plt.plot(sizes, average, label=f"{sorting_algorithm} - Average Case", linestyle='-')
    plt.plot(sizes, worst, label=f"{sorting_algorithm} - Worst Case", linestyle='-')

    # labels, title, and legend
    plt.xlabel('Input Size (N)')
    plt.ylabel('Time (seconds)')
    plt.title(f'{sorting_algorithm} - Time Complexity')
    plt.xscale('log')
    plt.yscale('log')

    # Adjust x-axis bounds
    plt.xlim(10, 5000000)

    # Adjust y-axis bounds
    plt.ylim(1e-6, 10)

    plt.legend()
    plt.grid(True)

    plt.show()

def create_table(sizes, best, average, worst, sorting_algorithm):
    plt.figure(figsize=(6, 4))

    table_data = [["Input Size (N)", "Best Case", "Average Case", "Worst Case"]] + \
                 list(zip(sizes, best, average, worst))
    table = plt.table(cellText=table_data, colLabels=None, loc='center', cellLoc='center', bbox=[0, 0, 1, 1])

    plt.axis('off')
    plt.title(f'{sorting_algorithm} - Time Complexity Data', fontsize=14)
    plt.show()

# Display plots and tables for each sorting algorithm
# ONLY RUN ONE PLOT AT A TIME DUE TO VARYING SIZES!

#create_plot(sizes, bubble_sort_best, bubble_sort_average, bubble_sort_worst, "Bubble Sort")
#create_table(sizes, bubble_sort_best, bubble_sort_average, bubble_sort_worst, "Bubble Sort")

create_plot(sizes, merge_sort_best, merge_sort_average, merge_sort_worst, "Merge Sort")
create_table(sizes, merge_sort_best, merge_sort_average, merge_sort_worst, "Merge Sort")

#create_plot(sizes, quick_sort_best, quick_sort_average, quick_sort_worst, "Quick Sort")
#create_table(sizes, quick_sort_best, quick_sort_average, quick_sort_worst, "Quick Sort")

# !!! NOTE: Will throw unhandled exception for null parameters, but still plots correctly !!!
#create_plot(sizes, None, None, quick_sort_slow, "Quick Sort (Slow)")
#create_table(sizes, None, None, quick_sort_slow, "Quick Sort (Slow)")

#create_plot(sizes, tim_sort_best, tim_sort_average, tim_sort_worst, "Tim Sort")
#create_table(sizes, tim_sort_best, tim_sort_average, tim_sort_worst, "Tim Sort")