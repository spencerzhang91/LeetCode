#147 InsertionSort_20151107

def InsertionSort(array):
    '''
    Array based implementation
    '''
    count = len(array)
    for i in range(1, count):
        key = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > key:
                array[j+1] = array[j]
                array[j] = key
            j -= 1
            print(array)
    return array


ls = [100,20,30,8,3]
print(ls)
InsertionSort(ls)

                
            
                
        
    
