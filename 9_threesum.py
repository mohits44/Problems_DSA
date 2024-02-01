# solution correct only output not there in platform(cj issue)
def findTriplets(arr, n, k):
    lst=[]
    found=False
    # Write your code here.
    for i in range (0,n):
        for j in range(i+1,n):
            for m in range(j+1,n):
                if arr[i]+arr[j]+arr[m]==k:
                    lst.append(arr[i])
                    lst.append(arr[j])
                    lst.append(arr[m])
                    found=True
                    break
            if found==True:
                break
        if found==True:
            break
    return lst
arr=[10, 5, 5, 5, 2]
print(findTriplets(arr,len(arr),12))
