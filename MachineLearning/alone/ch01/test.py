from random import *
import matplotlib.pyplot as plt
import numpy as np

bream_length = [round(random(),2)*10 + 20 + i  for i in range(1,36)]
bream_weight = [randint(50,100) + 150 + i * randint(10,15) for i in range(1,36)]
# bream_length.sort()
# bream_weight.sort()

print(bream_length)
print(bream_weight)

smelt_length = [round(random(),1) + 9 + i/2 for i in range(1,15)]
# smelt_length.sort()
# print(smelt_length)

smelt_weight = [round(random(),1)* 10 + 9 + i for i in range(1,15)]
# smelt_weight.sort()
# print(smelt_weight)

length = bream_length + smelt_length
weight = bream_weight + smelt_weight
fish_data = [[l,w] for l,w in zip(length,weight)]


plt.scatter(length,weight)

plt.xlabel('length')
plt.ylabel('weight')
plt.show()