# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # empty list to drop sorted stuff into (delelted starter code...)
    merged_arr = []
    # compare first elements of each. adds smaller to merged list.
    while len(arrA) != 0 and len(arrB) != 0: # go until one runs out ...
        if arrA[0] <= arrB[0]: #if same or A is smaller, add to merged and remove from A
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else: #otherwise, B must be smaller... so same thing for B
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    #if we exited the loop, then whatever is left of either should be added to merged
    # print(arrA, arrB)
    if len(arrB) == 0:
        merged_arr.extend(arrA)
    if len(arrA) == 0:
        merged_arr.extend(arrB)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Base-case is if an input list is just 1 element
    if len(arr) == 1:
        return arr
    # ALso possible the input list is nothing...
    elif len(arr) == 0:
        return arr
    # Recussion: chop and merge until base-case
    else:
        arrA = merge_sort(arr[:len(arr)//2])
        arrB = merge_sort(arr[len(arr)//2:])
    
    return merge(arrA, arrB)





# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
