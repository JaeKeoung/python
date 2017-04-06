a=[1,4,6,344,65,33,90,17,85]
b=len(a)
for j in range(0,b):
    for i in range(0,b-1):
        if a[i]>a[i+1]:
            temp=a[i+1]
            a[i+1]=a[i]
            a[i]=temp
print(a);
