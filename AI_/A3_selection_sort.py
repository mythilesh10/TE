
def selectionSort(arr):
    for i in range(len(arr)):
        min = float('-inf')
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    return arr
    
print(selectionSort([89,56,45,34,65,76])) #giving direct input


# OR with taking input 

# def selection_sort(arr):
#     for i in range(n-1):
#         min_index = i
        
#         # Find the minimum element in the unsorted part of the array
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
        
#         # Swap the minimum element with the first element of the unsorted part
#         arr[i], arr[min_index] = arr[min_index], arr[i]
    
#     return arr

# n = int(input("Enter number of elements: "))
# arr = []
# for i in range(n):
#     element = int(input("Enter element {} :".format(i+1)))
#     arr.append(element)


# sorted_arr = selection_sort(arr)
# print("Sorted array: ",sorted_arr)    