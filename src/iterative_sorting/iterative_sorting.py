# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        # begin with assumption that i is smallest
        current_at = i
        smallest_at = current_at
        # Looks ahead to each consecutive value after i in the list
        # if j-term is smaller than i-term, declares j smallest
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_at]:
                smallest_at = j
        
        # swaps places iff smallest is different than current
        # otherwise nothing -- assigns itself to itself
        arr[i], arr[smallest_at] = arr[smallest_at], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # iterate through list
    for i in range(len(arr)):

        for j in range(len(arr)-1):
            # kind of wonky, but j has to be 1 less than list times
            # want to start at i+1, and end at j+1
            j += 1
            if arr[j-1] > arr[j]:
                # swap values iff left term is bigger than right
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr