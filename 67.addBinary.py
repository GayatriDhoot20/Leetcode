class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=="0" and b=="0":
            return "0"
        bin_a = self.convert_binary(a)
        bin_b = self.convert_binary(b)
        add = bin_a+bin_b

        sum_add = self.convert_decimal(add)
        return sum_add[::-1]

    def convert_binary(self, var):
        rev_var = str(var[::-1])
        sum_var=0
        for i in range(len(rev_var)):
            sum_var = sum_var+int(rev_var[i])*pow(2,i)
        return sum_var

    def convert_decimal(self, var):
        sum_add=""
        while (var >=1):
            temp = var//2
            reminder = var%2
            sum_add = sum_add+str(reminder)
            var = temp
        return sum_add


obj1 = Solution()
print(obj1.addBinary("111", "11"))
print(obj1.addBinary("0", "0"))

