'''import time
#conta o tempo do cod
a=0
x=time.perf_counter()
while a<10000:
    print(a)
    a+=1
y=time.perf_counter()
print(y-x)'''

# importing enum for enumerations

# importing enum for enumerations
import enum
 
# creating enumerations using class
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3
 
# Comparison using "is"
if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")
 
# Comparison using "!="
if Animal.lion != Animal.cat:
    print("Lions and cat are different")
else:
    print("Lions and cat are same")
