import math 
import csv

with open('data.csv',newline='') as f:
    reader = csv.reader(f)   
    file_data = list(reader)

data = file_data[0]

def mean(data):
    total = 0
    n = len(data)

    for x in data:
        total += int(x)

    mean = total/n 
    return mean 

squaredList = []

for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredList.append(a)

sum = 0

for i in squaredList:
    sum += i

result = sum/(len(data)-1)
std = math.sqrt(result)

print(std)