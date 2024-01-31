# i/p: n=234
# prod-sum
# o/p: 15
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        summ=0
        while n!=0:
            digit=n%10
            prod=prod*digit
            summ=summ+digit
            n=n//10
        return prod-summ
obj=Solution()
print(obj.subtractProductAndSum(234))
