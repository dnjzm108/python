import tensorflow as tf  # 구글이 15년 오픈소스로 공개한 딥러닝 라이브러리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

주가 = [np.random.randint(10, 50) + i*2 for i in range(100)]

# plt.plot(np.arange(1,101),주가)
# plt.show()

# 독립 : 원인이 되는 값
# 종속 : 우리가 알고 싶은 값

독립 = pd.DataFrame(np.arange(1, 101))
종속 = pd.DataFrame(주가)
독립.shape, 종속.shape


X = tf.keras.layers.Input(shape=[1])  # 독립변수 col
Y = tf.keras.layers.Dense(1)(X)  # 종속변수의 col (뉴런의 개수)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')  # MSE (Mean Squared error)

model.fit(독립, 종속, epochs=10000, verbose=0)
model.fit(독립, 종속, epochs=10)

test = model.predict([50])
test2 = model.predict([40])
print('test : ', test)
print('test2: ', test2)

# plt.plot(np.arange(1,101),주가)
# plt.plot(np.arange(1,101),2.019 * np.arange(1,101)+23.739)
# plt.show()

오차값 = 종속 - model.predict(독립)
print('오차값 : ', 오차값)

오차값의제곱 = 오차값 ** 2
print('오차값의제곱 : ', 오차값의제곱)

오차mse = (오차값의제곱.sum())/100  # mse  오차 평균
print('오차mse : ', 오차mse)


두수의곱 = 독립 * 종속
int(100 * 두수의곱.sum())

int(독립.sum() * 종속.sum())

int(100*(독립 ** 2).sum())

int(독립.sum()*독립.sum())

분자 = int(100 * 두수의곱.sum()) - int(독립.sum() * 종속.sum())
분모 = int(100 * (독립 ** 2).sum()) - int(독립.sum() * 독립.sum())

# print('분자/분모 : ',분자/분모)

mo = model.get_weights()
# print(mo)




