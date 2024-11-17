class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        y = str(x)
        if x < 0:
            sign = -1
            y = str(abs(x))   
        rev = ""
        for i in range(len(y)):
            rev += y[(-1-i)]
            ret = int(rev)*sign
            if ret < -1*2**31/10 or ret >= 2**31/10:
                if i != len(y)-1:
                    return 0 
        return ret
