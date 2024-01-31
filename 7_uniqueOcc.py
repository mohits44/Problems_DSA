
# s="book"
# d={}
# for i in s:
    # d[#iss bracket m vo cheez jayegi jo aap key banana chahte ho]

# get method value assosciated with the key return karta hai

# s="book"
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
#     print(d)

# a=[1,2,2,3,3,3]
# b=set(a)
# print(b)

#//problem starts here
# i/p: arr=[1,2,2,1,1,3]  1,2,2,3,3,3,4,4   1,2,3,2
# o/p: true


class Solution:
    def uniqueOccurrences(self, arr):
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        if len(d.values())==len(set(d.values())):
            return True 
        else:
            return False
a=Solution()
b=[1,2,2,1,1,3]
print(a.uniqueOccurrences(b))
