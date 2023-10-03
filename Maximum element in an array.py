
def find_maximum(arr):
    
    max_element = arr[0]


    for element in arr:
        if element > max_element:
            max_element = element

    return max_element

#Example using the find_maximum function

my_array = [12, 45, 78, 34, 56, 89, 23]
max_value = find_maximum(my_array)
print("Maximum element:", max_value)
