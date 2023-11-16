"""
Implementation of the heapsort algorithm to sort a given list.

Functions:
- heapify(arr, n, i): Heapify subtree rooted at index i.
- build_max_heap(arr, n): Builds a max heap from an array.
- heapsort(arr): Sorts an array using the heapsort algorithm.
"""
def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i.
    
    Args:
    arr (list): List to be sorted.
    n (int): Size of heap.
    i (int): Index of subtree root.
    """
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    
    if (l < n) and arr[largest] < arr[l]:
        largest = l
        
    if (r < n) and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Swap
        
        heapify(arr, n, largest)


def build_max_heap(arr, n):
    """
    Builds a max heap from an array.

    Args:
    arr (list): The array to be converted into a max heap.
    n (int): The size of the array.

    Returns:
    list: The max heap.
    """
    for i in reversed(range(n//2)):
        heapify(arr, n, i)
        
    return arr


def heapsort(arr):
    """
    Sorts an array using the heapsort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    n = len(arr)
    
    arr = build_max_heap(arr, n)
    
    for i in reversed(range(n)):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
    return arr 