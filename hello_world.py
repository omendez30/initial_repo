
import random
import sys
import os

print("Hello World")

x = 1
y = 3
name = "taco"

if x > y:
    print("x is greater than y")
else:
    print("x is less than y")
    
print(random.randint(0,9))

print(id(name), type(name))

for i in range(1,5):
    print(i)
print(f"This is outside of the for loop {i}", end='\n')


favorite_num = 9
def testing_scope():
    x = 'cat'
    y = 'dog'
    print(f'My favorite number is {favorite_num}')
    
    def new_local_scope():
        z = 'Panda'
        print('New Scope')
        x = 150
        print(x, y, z, favorite_num)
    x = new_local_scope()
    print(x)
        
testing_scope()
print(2**2 == 4)
print('big' > 'small')
print(11%5)
print((10>=5*2) and (10 <= 5*2))

print("Making a new string to add to this repo.")