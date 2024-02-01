# each item either appears once or twice
# make a list of those that appears twice
# items methods of dictionary is useful here

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
class Solution:
    def findDuplicates(self, nums):
        d={}
        lst=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for key,value in d.items():
            if value==2:
                lst.append(key)
        return lst
nums=[4,3,2,7,8,2,3,1]
obj=Solution()
print(obj.findDuplicates(nums))
