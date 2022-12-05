# -*- coding: utf-8 -*-
"""혼자하는 머신러닝+딥러닝.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lBcTGP_j16dcTO7K4kPHPSj54MYRBBQX
"""

import sklearn
# import tensorflow
import matplotlib.pyplot as plt
import random

"""2개의 클래스 (class)
분류(classfication)
이진 분류(binary classfication)
"""

# 샘플 준비 도미 와 빙어
# 도미 샘플
bream_length = [round(random.random(),1) +20 + i/2  for i in range(1,36)]
bream_weight = [random.randint(1,100) * 4 + 250 + i * 2  for i in range(1,36)]
bream_length.sort()
bream_weight.sort()

# 빙어 샘플
smelt_length = [round(random.random(),1) + 9 + i/2 for i in range(1,15)]
smelt_length.sort()
smelt_weight = [round(random.random(),1)* 10 + 9 + i/2 for i in range(1,15)]
smelt_weight.sort()

# # scatter plot  산점도 
# plt.scatter(bream_length,bream_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# 리스트 합치기
length = bream_length + smelt_length
weight = bream_weight + smelt_weight
fish_data = [[l,w] for l,w in zip(length,weight)]

# 정답 준비
fish_target = [1]*35 + [0]*14

# k-최근접 이웃
from sklearn.neighbors import KNeighborsClassifier

# 모델
kn = KNeighborsClassifier()

kn.fit(fish_data, fish_target)

kn.score(fish_data, fish_target)

kn.predict([[30,600]])

kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(fish_data,fish_target)
kn49.score(fish_data,fish_target)
# print(35/49) 확률

