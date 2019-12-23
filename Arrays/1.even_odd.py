'''
Reorder entries in an array so that even entries appear first
without using any additional data structure
'''

#with additional array

def even_odd(array):
    even = []
    odd = []
    for num in array:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    even.extend(odd)

    return even

# without using additional data structure

def even_odd_wo(array):
    '''
    here we have to pointer to the array(front and back)
    we start from the start of the array
    if the element at the start of the array is even
    we move the pointer forward
    if the element is odd we swap elements from two pointer in the array
    '''
    start , end = 0 , len(array)-1

    while(start < end):
        if array[start] % 2 == 0:
            start += 1
        else:
            array[start], array[end] = array[end], array[start]
            end -= 1
    return array


print(even_odd_wo([3,2,5,6,8,1,7,10,9,4]))
