# Input: n = 00000000000000000000000000001011 //signed integer hai
# Output: 3
# meanning: teen ek hai bits m
# anyBit&1=anyBit (0&1=1, 0&0=0)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n!=0:
            if n&1==1:
                count+=1
            n=n>>1
        return count
obj=Solution()
print(obj.hammingWeight(11))
