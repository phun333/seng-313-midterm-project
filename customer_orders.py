import csv
import time

# read CSV file
def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        orders = [row for row in csv_reader]
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

# measure pperformance
def measure_performance(sort_func, data, key):
    start_time = time.time()
    sorted_data = sort_func(data, key)
    end_time = time.time()
    return sorted_data, end_time - start_time

# main function
# ask user to select dataset
def main():
    print("\n********** Datasets **********")
    print("1. Small Dataset (10 rows)")
    print("2. Medium Dataset (100 rows)")
    print("3. Large Dataset (1000 rows)")
    print("4. Extra Large Dataset (10000 rows)")
    print("5. Exit")
    
    user_input = input("\nEnter your choice: ")
    
    if user_input == '1':
        file_path = 'datasets/customer_orders_datasets/customer_orders.csv'
    elif user_input == '2':
        file_path = 'datasets/customer_orders_datasets/customer_orders1.csv'
    elif user_input == '3':
        file_path = 'datasets/customer_orders_datasets/customer_orders2.csv'
    elif user_input == '4':
        file_path = 'datasets/customer_orders_datasets/customer_orders3.csv'
    elif user_input == '5':
        print("Exiting program.")
        return
    else:
        print("Invalid choice! Please try again.")
        return

    # read the selected dataset
    orders = read_csv(file_path)
    
    # measure quick sort performance
    quick_sorted_orders, quick_sort_time = measure_performance(quick_sort, orders, 'Order Amount')
    print(f"\nQuick Sort Time: {quick_sort_time:.6f} seconds")
    
    # measure merge sort performance
    merge_sorted_orders, merge_sort_time = measure_performance(merge_sort, orders, 'Order Amount')
    print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
    
    # this is to verify that both sorting algorithms are working correctly
    
    # print top 5 sorted orders for verification
    print("\nTop 5 Orders by Quick Sort:")
    for order in quick_sorted_orders[:5]:
        print(order)
    
    print("Top 5 Orders by Merge Sort:")
    for order in merge_sorted_orders[:5]:
        print(order)
    # compare the performance of quick sort and merge sort
    if (quick_sort_time < merge_sort_time):
        print("\nQuick Sort is faster than Merge Sort.")
    else:
        print("\nMerge Sort is faster than Quick Sort.")

if __name__ == "__main__":
    main()
