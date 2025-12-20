class Solution(object):
    def addDigits(self, num):
        while num>=10:
            num=sum(map(int,str(num)))
        return num