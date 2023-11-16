"""
Implementation of the mergesort algorithm to sort a given list.

Functions:
    merge(arr, start, mid, end):
        Merge two sorted subarrays of arr[].
        
    mergesort(arr, start, end):
        Sorts the given array using the mergesort algorithm.
"""
def merge(arr, start, mid, end):
    """
    Merge two sorted subarrays of arr[].
    
    Parameters:
    arr (list): List to be sorted
    start (int): Starting index of first subarray
    mid (int): Ending index of first subarray
    end (int): Ending index of second subarray
    
    Returns:
    None
    """
    size_left = mid - start + 1
    size_right = end - mid
    
    left = arr[start : start + size_left].copy()
    right = arr[mid + 1 : mid + 1 + size_right].copy()
    
    pos_left = pos_right = 0
    pos_arr = start
    
    while (pos_left < size_left and pos_right < size_right):
        if (left[pos_left] <= right[pos_right]):
            arr[pos_arr] = left[pos_left]
            pos_left += 1
            
        else:
            arr[pos_arr] = right[pos_right]
            pos_right += 1
            
        pos_arr += 1
        
    while (pos_left < size_left):
        arr[pos_arr] = left[pos_left]
        pos_left += 1
        pos_arr += 1
        
    while (pos_right < size_right):
        arr[pos_arr] = right[pos_right]
        pos_right += 1
        pos_arr += 1
        
    return arr


def mergesort(arr, start, end):
    """
    Sorts the given array using the mergesort algorithm.

    Args:
        arr (list): The array to be sorted.
        start (int): The starting index of the array to be sorted.
        end (int): The ending index of the array to be sorted.
    """
    if start < end:
        mid = (start + end) // 2

        mergesort(arr, start, mid)
        mergesort(arr, mid + 1, end)

        arr = merge(arr, start, mid, end)

    return arr