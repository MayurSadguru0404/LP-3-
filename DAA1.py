n=int(input("Enter the number of terms:"))
a,b=0,1

for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print(f"\n Steps :{n}")

#Revursive
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter NUmber:"))
for i in range(n):
    print(fibonacci(i),end=" ")