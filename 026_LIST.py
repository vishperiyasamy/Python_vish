#list in python

"""
sequence type
mutable
a[5]
a={1,2,3,4,5}
a[0]=1

"""
a=[1,2,3,4,5]
print(a)
print(type(a))

a[2]=23
print(a)#mutable

print(a[1])

#list slicing

print(a[-1])

print(a[0:3])

print(a[2:])

print(a[:3])

# python array is hetrogenous
print("-----------------")

a=[1,True,'vish',2.5,[1,2,3,4,5]]

print(a)
print(type(a))

print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))

print(a[4])
print(a[4][3])

print("----------------")
a=[1,2,3,4,5]
print(a)
a.clear()#clear function
print(a)

b=a.copy()#copy function
print(b)

a=[2,3,5,6,7,2,5,3,3,3]
print(a.count(3))#counr function

a=[1,2,3,4,5]
print(a.index(1))#index take first only

print(len(a))#length function

print(max(a))#maxmimum

print(min(a))#minimum function

print(a)
a.pop(0)#remove elements using index

a=[1,2,3,4,5]
print(a.remove(3))#it can remove first occurence only

print("------------------")
names=["vish"]
names.append("kutty")
names.append("chlm")
print(names)

names2=["cutei","pie"]
names.extend(names2)
print(names)


names.insert(1,"sai")
print("names")

print("--------")
print(list(range(7)))#list constructors
print(list("vishkutty"))

a=[1,5,10,25,100,15,38]
a.sort()#ascnedning
print(a)

a.sort(reverse=True)#descending
print(a)

a=["orange","mango","apple"]
a.sort()#ascnedning
print(a)

a.sort(reverse=True)#descending
print(a)

print("************")

a=["orange","mango","apple"]
a.sort(key=len)#ascnedning using key
print(a)