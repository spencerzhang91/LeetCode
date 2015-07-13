class Solution:
    def romanToInt(self, string):
        double_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        single_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
        res = 0
        remove_list = []
        for key in double_dict.keys():
            if key in string:
                res += double_dict[key]
                remove_list.append(key)
        print(remove_list)
        print(res)
        for key in remove_list:
            string = string.replace(key, '')
        print(string)
        for s in string:
            res += single_dict[s]
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.romanToInt('MMCMXCIX'))
            
