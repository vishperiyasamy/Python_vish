
#tuple is immutable
#it can be surrounded by ()

a=(1,2.9,True,"ram")
print(a)
print(type(a))

#accesing using  index
print(a[2])
print(a[-1])
#range
print(a[0:2])
print(a[:3])
#convert tuple into list
b=list(a)
print(b)
b.append("raja")
print(b)
print(type(b))
#convert list in tuple
a=tuple(b)
print(a)
print(type(a))
#using for loop
for i in a:
    print(i)

#if statement
    if "raj" in a:
        print("raja is foubnd")
    else:
        print("not found")
#length
        print(len(a))
#single item
        a=(1,)
        print(type(a))
#delete
        #del a
#add two tuple
a=(1,2,3,4)
b=(5,6,7,8,3)
c=a+b
print(a)
#count
print(c.count(3))
#nested tuple
a=(1,2,3,4)
b=(5,6,7,8,3)
c=(a,b)
print(c)
print(c[1])
print(c[0])
print("------------")
print(c[0][1])
#replication
x=('vish',)*10
print(x)
#max&min
a=(1,5,8,9)
print(min(a))
print(max(a))
