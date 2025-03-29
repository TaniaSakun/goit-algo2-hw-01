import random

def find_max_min(arr):
    """
    Determine the minimum and maximum elements in an array using a divide-and-conquer approach.
    """
    if not arr:
        raise ValueError("Input array must not be empty")
    
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return min(arr), max(arr)
    
    mid = len(arr) // 2
    left_min, left_max = find_max_min(arr[:mid])
    right_min, right_max = find_max_min(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

def find_nth_smallest(arr, n):
    """
    Locate the k-th smallest element in an unsorted array using the Quickselect algorithm.
    """
    if not arr:
        raise ValueError("Input array must not be empty")
    
    if n < 0 or n >= len(arr):
        raise IndexError("k is out of bounds")
    
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if n < len(left):
        return find_nth_smallest(left, n)
    elif n < len(left) + len(middle):
        return pivot
    else:
        return find_nth_smallest(right, n - len(left) - len(middle))

def generate_random_array(size, lower=-100, upper=100):
    """Generates a random list of numbers within a specified range."""
    return [random.randint(lower, upper) for _ in range(size)]

def main():
    """Main function to execute tasks."""
    print("\nTask 1: Identifying the minimum and maximum elements in an array")
    arr = generate_random_array(16)
    print("Array:", arr)
    min_element, max_element = find_max_min(arr)
    print(f"Minimum element: {min_element}, Maximum element: {max_element}")
    
    print("\nTask 2: Finding the k-th smallest element")
    arr = generate_random_array(16)
    print("Array:", arr)
    k = random.randint(0, len(arr) - 1)
    kth_element = find_nth_smallest(arr, k)
    print(f"{k}-th smallest element: {kth_element}")

if __name__ == "__main__":
    main()