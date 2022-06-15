import random 
import math 
numList = [] 
circle = 0 
square = 0 

iteration = int(input("Iterations?"))

for i in range (iteration): 
	numList.append({"x": random.uniform(0,1), "y": random.uniform(0,1)})
	if math.sqrt(abs(numList[i-1]['x'])**2+abs(numList[i-1]['y'])**2)<= 1:
		circle += 1
	else: 
		square += 1

print (circle)
print (square)
print ((circle/(circle+square))*4)
print (numList)
