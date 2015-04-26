'''
Using a cmp_to_key function to make it possible to sort a list by iterating
a function over every two items in the list and sort them according to the result.
'''
class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        nums_string = [str(num) for num in nums]        
        nums_string.sort(reverse = True, key = cmp_to_key(self.compare))
        res = ''.join(nums_string)
        return res if int(res) != 0 else '0'

    def compare(self, a, b):
        if a+b > b+a:
            return 1
        elif a+b < b+a:
            return -1
        else:
            return 0
            

if __name__ == "__main__":
    test = Solution()
    print(test.largestNumber([9,91,95,85,8]))



