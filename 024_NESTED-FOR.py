# Nested For Loop
"""
*
**
***
****
*****

*****
****
***
**
*

ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

A-Z => 65-90
a-z=> 97-122

"""

for i in range(6):
    for j in range(i):
        print("*",end="")# end ="" it can for run in single line
    print("")#new line
print("----------------")

for i in range(5,0,-1): #0 ku munnadi varaikum it can print
    for j in range(i):
        print("*",end="")
    print("")
print("----------------")

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")#for convert int to chraracter we cn use chr(j)
    print("")