import tensorflow as tf  # 구글이 15년 오픈소스로 공개한 딥러닝 라이브러리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

광고액 = [np.random.randint(10, 50)+ np.log(i*5) * 50 for i in range(1, 101)]
계절성 = [np.sin(i/3)*100 + i*3 + j*2 for i, j in zip(np.arange(1, 101), 광고액)]
매출액 = [i ** (np.log(np.log(i))) + j for i, j in zip(np.arange(1, 101), 계절성)]

# plt.plot(np.arange(1, 101), 광고액, label='a')
# plt.plot(np.arange(1, 101), 계절성, label='b')
# plt.plot(np.arange(1, 101), 매출액, label='c')

# plt.legend()
# plt.show()

독립 = pd.DataFrame({
    '계절성': 계절성,
    '광고액': 광고액
})
종속 = pd.DataFrame({
    '매출액': 매출액
})
독립.shape, 종속.shape


# 모델 준비
X = tf.keras.layers.Input(shape=[2])  # 독립변수의 col
H = tf.keras.layers.Dense(200, activation='swish')(X)  # 노드의 수는 천천히 늘려감(2~200)
H = tf.keras.layers.Dense(5,activation='swish')(H) # 처음에는 주석 처리
Y = tf.keras.layers.Dense(1)(H)  # 종속변수의 col
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')  # MSE(Mean squared error)

model.fit(독립, 종속, epochs=10000, verbose=0)
model.fit(독립, 종속, epochs=10)

# 히든 레이어 1개의 노드의 개수가 2개

# 히든 레이어 1개의 노드의 개수가 200개 
plt.plot(np.arange(1,101),model.predict(독립),label='예측값')
plt.plot(np.arange(1,101),종속,label='실제값')

plt.legend()
plt.show()