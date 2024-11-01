import csv
import time
import matplotlib.pyplot as plt

# read CSV file
def read_csv(file_path):
    catalog = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            catalog.append(row)
    return catalog

# linear search implementation
# approach : list comprehension
def linear_search(catalog, search_term):
    return [product for product in catalog if search_term.lower() in product['Product Name'].lower()]

# binary search implementation
# approach : iterative binary search
def binary_search(catalog, search_term):
    catalog.sort(key=lambda x: x['Product Name'].lower())
    left, right = 0, len(catalog) - 1
    results = []
    while left <= right:
        mid = (left + right) // 2
        if search_term.lower() in catalog[mid]['Product Name'].lower():
            results.append(catalog[mid])
            # Check for other matches around the mid point
            l, r = mid - 1, mid + 1
            while l >= left and search_term.lower() in catalog[l]['Product Name'].lower():
                results.append(catalog[l])
                l -= 1
            while r <= right and search_term.lower() in catalog[r]['Product Name'].lower():
                results.append(catalog[r])
                r += 1
            break
        elif search_term.lower() < catalog[mid]['Product Name'].lower():
            right = mid - 1
        else:
            left = mid + 1
    return results

# measure performance
def measure_performance(search_function, catalog, search_term):
    start_time = time.time()
    results = search_function(catalog, search_term)
    end_time = time.time()
    return results, end_time - start_time

# main function
if __name__ == "__main__":
    small_catalog = read_csv('datasets/product_catalog_datasets/product_catalog.csv')
    medium_catalog = read_csv('datasets/product_catalog_datasets/product_catalog1.csv')
    large_catalog = read_csv('datasets/product_catalog_datasets/product_catalog2.csv')
    extra_large_catalog = read_csv('datasets/product_catalog_datasets/product_catalog3.csv')
    
    search_term = input("Enter the product name to search: ") # search term that may or may not exist


    # measure performance for linear search
    small_linear_results, small_linear_time = measure_performance(linear_search, small_catalog, search_term)
    medium_linear_results, medium_linear_time = measure_performance(linear_search, medium_catalog, search_term)
    large_linear_results, large_linear_time = measure_performance(linear_search, large_catalog, search_term)
    extra_large_linear_results, extra_large_linear_time = measure_performance(linear_search, extra_large_catalog, search_term)

    # measure performance for binary search
    small_binary_results, small_binary_time = measure_performance(binary_search, small_catalog, search_term)
    medium_binary_results, medium_binary_time = measure_performance(binary_search, medium_catalog, search_term)
    large_binary_results, large_binary_time = measure_performance(binary_search, large_catalog, search_term)
    extra_large_binary_results, extra_large_binary_time = measure_performance(binary_search, extra_large_catalog, search_term)

    # print the number of results found for each search
    print("Small Dataeset")
    print(f"Linear Search - Small Catalog: {len(small_linear_results)} results found in {small_linear_time} seconds")
    print(f"Binary Search - Small Catalog: {len(small_binary_results)} results found in {small_binary_time} seconds\n")
    print("Medium Dataeset")
    print(f"Linear Search - Medium Catalog: {len(medium_linear_results)} results found in {medium_linear_time} seconds")
    print(f"Binary Search - Medium Catalog: {len(medium_binary_results)} results found in {medium_binary_time} seconds\n")
    print("Large Dataeset")
    print(f"Linear Search - Large Catalog: {len(large_linear_results)} results found in {large_linear_time} seconds")
    print(f"Binary Search - Large Catalog: {len(large_binary_results)} results found in {large_binary_time} seconds\n")
    print("Extra Large Dataeset")
    print(f"Linear Search - Extra Large Catalog: {len(extra_large_linear_results)} results found in {extra_large_linear_time} seconds")
    print(f"Binary Search - Extra Large Catalog: {len(extra_large_binary_results)} results found in {extra_large_binary_time} seconds")

    # plotting the results
    sizes = ['Small', 'Medium', 'Large', 'Extra Large']
    linear_times = [small_linear_time, medium_linear_time, large_linear_time, extra_large_linear_time]
    binary_times = [small_binary_time, medium_binary_time, large_binary_time, extra_large_binary_time]

    plt.plot(sizes, linear_times, label='Linear Search')
    plt.plot(sizes, binary_times, label='Binary Search')
    plt.xlabel('Dataset Size')
    plt.ylabel('Search Time (seconds)')
    plt.title('Search Algorithm Performance Performance')
    plt.legend()
    plt.show()
