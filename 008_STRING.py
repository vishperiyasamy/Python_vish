# String And String Function
s = "vish kutty"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("t"))
print(s.endswith("ty"))
print(s.find("s"))
print(s.find("t", 7))
print(s.replace("o", '0'))


a = "vish1234"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())

s = "he\nis\ngood"
print(s)
print(s.splitlines()) #for list
print(s.splitlines(True)) # it can come with \n

a = "viswa Computer Education"# we can split the space
print(a.split(" "))

a = "vishr,kutty,Computer,Education"
print(a.split(","))

s="    vish    " #length strip remove function
print(len(s))
print(len(s.strip()))
print(len(s.lstrip())) #left side reomve space
print(len(s.rstrip()))#reigth side remove space

s='12-03-2020'
print(s.partition('-'))