n=int(input("Enter the Nth term: "))
if n%2 ==0 :
    n1=n//2
    n2=n/2
else:
    n1=(n+1)//2
    n2=(n-1)//2
#fibonacci
f=[]
t1=0
t2=1
i=0
f.append(t1)
f.append(t2)
while(i< n1-2):
    s=t1+t2
    f.append(s)
    t1=t2
    t2=s
    i=i+1
print(f)
#prime
p=[]
i=2
countp=1
while (countp <= n2) :
    flag=1
    for j in range (2,(i//2+1)):
        if(i%j==0):
            flag=0
            break
    if (flag==1):
        p.append(i)
        countp+=1
    i+=1
print (p)
total=[]
k=0
even=0
odd=0
for k in range (0,n):
    if (k%2==0):
        #print (even)
        #print (odd)/print(f[even])
        total.append (f[even])
        even+=1
    else:
        #print (odd)
        #print (even)/print(p[odd])
        total.append (p[odd])
        odd+=1
print(total)
