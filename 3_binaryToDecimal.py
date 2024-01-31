# btoD binary to decimal
# input format
# 2            //2 tescases
# 7            //string length
# '1010101'    //1+4+16+64=85
# 4          //string length
# '1011'      //1+2+8=11

# given a binary number as a string 'str' of size 'n'
# convert it into its decimal equivalent 

def convert(n, str):
    j=0
    summ=0
    for i in str:
        if i=='1':
            summ=summ+2**j
        j+=1
    return summ
print(convert(7,'1010101'))
