# a=int(input("Enter the range in which u want to check prime  :- "))
# b=int(input(':-'))
a=900
b=950
y=[]

for x in range(a,b+1):
    if x > 1:

        for i in range(2, x):
            print("checking ", x ,i)
            if (x % i) == 0:
                break


print(y)


