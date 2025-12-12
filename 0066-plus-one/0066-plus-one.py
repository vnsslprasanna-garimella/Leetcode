class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0   # set to 0 if digit was 9
        
        # If all digits were 9
        return [1] + digits
