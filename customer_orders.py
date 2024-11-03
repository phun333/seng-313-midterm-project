import csv
import time
import matplotlib.pyplot as plt

# read CSV file
def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            orders = []
            orders.append(row)
    return orders

# quick sort implementation
# approach : quicksort using list comprehension
def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if float(x[key]) > float(pivot[key])]
    middle = [x for x in arr if float(x[key]) == float(pivot[key])]
    right = [x for x in arr if float(x[key]) < float(pivot[key])]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# merge sort implementation
# approach : merge sort using recursion
def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if float(left[i][key]) > float(right[j][key]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# measure performance
def measure_performance(sort_func, data, key):
    start_time = time.time()
    sorted_data = sort_func(data, key)
    end_time = time.time()
    return sorted_data, end_time - start_time

# plot performance
def plot_performance(quick_sort_times, merge_sort_times, dataset_sizes):
    plt.figure(figsize=(10, 6))
    plt.plot(dataset_sizes, quick_sort_times, marker='o', label="Quick Sort")
    plt.plot(dataset_sizes, merge_sort_times, marker='o', label="Merge Sort")
    plt.xlabel("Dataset Size (rows)")
    plt.ylabel("Time (seconds)")
    plt.title("Quick Sort vs Merge Sort Performance")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("\n********** Datasets **********")
    print("1. Small Dataset (10 rows)")
    print("2. Medium Dataset (100 rows)")
    print("3. Large Dataset (1000 rows)")
    print("4. Extra Large Dataset (10000 rows)")
    print("5. Performance Chart for All Datasets")
    print("6. Exit")
    
    user_input = input("\nEnter your choice: ")
    
    dataset_files = [
        'datasets/customer_orders_datasets/customer_orders.csv',
        'datasets/customer_orders_datasets/customer_orders1.csv',
        'datasets/customer_orders_datasets/customer_orders2.csv',
        'datasets/customer_orders_datasets/customer_orders3.csv'
    ]
    dataset_sizes = [10, 100, 1000, 10000]
    
    if user_input in ['1', '2', '3', '4']:
        file_path = dataset_files[int(user_input) - 1]
        orders = read_csv(file_path)
        
        # measure quick sort performance
        quick_sorted_orders, quick_sort_time = measure_performance(quick_sort, orders, 'Order Amount')
        print(f"\nQuick Sort Time: {quick_sort_time:.20f} seconds")
        
        # measure merge sort performance
        merge_sorted_orders, merge_sort_time = measure_performance(merge_sort, orders, 'Order Amount')
        print(f"Merge Sort Time: {merge_sort_time:.20f} seconds")
        
        # print top 5 sorted orders for verification
        print("\nTop 5 Orders by Quick Sort:")
        for order in quick_sorted_orders[:5]:
            print(order)
        
        print("\nTop 5 Orders by Merge Sort:")
        for order in merge_sorted_orders[:5]:
            print(order)
        
        # compare performance
        if quick_sort_time < merge_sort_time:
            print("\nQuick Sort is faster than Merge Sort.")
        else:
            print("\nMerge Sort is faster than Quick Sort.")
    
    elif user_input == '5':
        quick_sort_times = []
        merge_sort_times = []
        
        # measure and collect times for each dataset size
        for file_path in dataset_files:
            orders = read_csv(file_path)
            
            _, quick_sort_time = measure_performance(quick_sort, orders, 'Order Amount')
            _, merge_sort_time = measure_performance(merge_sort, orders, 'Order Amount')
            
            quick_sort_times.append(quick_sort_time)
            merge_sort_times.append(merge_sort_time)
        
        # plot performance
        plot_performance(quick_sort_times, merge_sort_times, dataset_sizes)
    
    elif user_input == '6':
        print("Exiting program.")
        return
    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
