# // reversing can cause rev to go outside 32 bit range
# // also -1 and largest unsigned int have same presentation

class Solution:
    def reverse(self, x: int) -> int:
        maxi=(2**31-1)/10
        mini=-((2**31)/10)
        if x==0:
            return 0
        y=0
        z=x
        x=abs(x)
        while x!=0:
            y=y*10+x%10

            if y/10>maxi or (-y/10<mini and z<0):
                return 0

            x=x//10
        if z>0:
            return y
        else:
            return -1*y
obj=Solution()
print(obj.reverse(-123))
