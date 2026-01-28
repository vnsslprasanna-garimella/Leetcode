class Solution:
    def divide(self, dividend, divisor):
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            # Double the divisor until it exceeds dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            # Subtract and add to quotient
            dividend -= temp_divisor
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        return quotient
