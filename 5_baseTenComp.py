# binary string to decimal ka logic
# instead of 1 apan 0 pe summ=summ+2^i karenge

# i/p:5  101
# o/p:2  010

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        i=0
        summ=0
        if n==0:            # edge case
            return 1
        while n!=0:
            if n&1==1:
                i=i+1
            else:
                summ=summ+2**i
                i=i+1
            n=n>>1
        return summ
obj=Solution()
print(obj.bitwiseComplement(5))
