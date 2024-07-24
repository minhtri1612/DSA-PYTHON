class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        
        if negative:
            reversed_num = -reversed_num
        
        
        return reversed_num

solution = Solution()
print(solution.reverse(987))  

print(solution.reverse(123))  
print(solution.reverse(-123)) 
print(solution.reverse(120))   
