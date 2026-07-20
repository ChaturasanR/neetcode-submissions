class Solution:
    def reverse(self, x: int) -> int:
        num_cpy = abs(x)
        reverse_num = 0
        while int(num_cpy/10) > 0:
            rem = num_cpy%10
            reverse_num *= 10
            reverse_num += rem
            num_cpy = int(num_cpy/10)
        
        reverse_num *= 10
        reverse_num += num_cpy%10
        if x < 0:
            reverse_num *= -1

        return 0 if reverse_num > pow(2, 31)-1 or reverse_num < -1*pow(2, 31) else reverse_num