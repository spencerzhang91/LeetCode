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
'''
rule breaking shameless approach below:
Final correct solution will be done within 20 minutes
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        array.sort()
        curr = head = ListNode(0) # the temp head
        for item in array:
            temp = ListNode(item)
            curr.next = temp
            curr = curr.next
        head = head.next
        return head
            
                
        
    
