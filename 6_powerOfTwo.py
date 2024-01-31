class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=0
        if n<0:        # //edge case
            return False
        if n==0:
            return False
        while n!=0:
            if n&1==1:
                count=count+1
            n=n>>1
        if count>1:
            return False
        else:
            return True
