user = {
    "name":"vish",
    "age":19,
    "isMarried":False
}

print(user)
print(type(user))
#access index
print(user["name"])
#don't put key two times it become error

#acces age
print(user.get('age'))
#get keys
print(user.keys())
#get values
print(user.values())
#get both key & values
print(user.items())

#for loop

for x in user:
    print(x," ",user[x])
    """
    print(x)
    print(user[x])
    """
#print only values
for x in user.values():
    print(x)
#print only keys
for x in user.keys():
    print(x)
#print itmes
for x,y in user.items():
    print(x,y)
#check valuse present in the items
if "name" in user:
    print("present")
#updated
user.update({"gender":"male"})
print(user)
#updated key
user["age"]=20
print(user)
#pop
user.pop("age")
print(user)
#clear all data
user.clear()
print(user)
#del() it can delete ditictionary4
#nested dictinoary
user = {
    "user1":{
    "name":"vish",
    "age":19,
    "isMarried":False
    },
    "user2" : {
    "name":"kutty",
    "age":20,
    "isMarried":True
    }
}
print(user)