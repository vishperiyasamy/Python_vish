a = """Thanjavur  also known as Thanjai, previously known as Tanjore,[1] is a city in Tamil Nadu. Thanjavur is the 11th biggest city in Tamil Nadu. Thanjavur is an important center of South Indian religion, art, and architecture. Most of the Great Living Chola Temples, which are UNESCO World Heritage Monuments, are located in and around Thanjavur. The foremost among these, the Brihadeeswara Temple, built by the Chola emperor Rajaraja I, is located in the centre of the city. Thanjavur is also home to Tanjore painting, a painting style unique to the region. Thanjavur is the headquarters of the Thanjavur District. The city is an important agricultural centre located in the Kaveri Delta and is known as the Rice bowl of Tamil Nadu. Thanjavur is administered by a municipal corporation covering an area of 128.02 km2 (49.43 sq mi) and had a population of 290,720 in 2011. 

"""
print(a)
print(type(a))
#multi line comments




vish = [20,33,44,55]
print(vish[0])
print(type(vish))

para=[]
print(type(para))
#list is a collection of values
print("Enter a para :")

while True: #endless loop
    line = input()
    if line: # data iruaknu pakkum input ku
        para.append(line)
    else:
        break
print(para)
output ='\n'.join(para)

print(output)