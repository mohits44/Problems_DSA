def sort012(arr, n) :

	# write your code here
    # don't return anything
    cntOne,cntTwo,cntZero=0,0,0 
    for i in arr:
        if i==0:
            cntZero+=1
        elif i==1:
            cntOne+=1
        else:
            cntTwo+=1
    for i in range(0,cntZero):
        arr[i]=0
    m=cntOne+cntZero
    for i in range(cntZero,m):
        arr[i]=1

    for i in range(m,n):
        arr[i]=2
arr=[1,2,0,0,1,2]
n=len(arr)
sort012(arr,n)
print(arr)
