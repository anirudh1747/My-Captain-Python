a=int(input("Enter the number of terms: "))
h=0                                     
j=1                                         
if a<=0:
    print(h)
else:
    print(h,j,end=" ")
    for x in range(2,a):
        y=h+j                           
        print(y,end=" ")
        h=j
        j=y
