# app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Linear Regression Visualizer")

# 參數控制
n_samples = st.slider("Number of samples", 10, 500, 100)
noise = st.slider("Noise level", 0.0, 50.0, 10.0)

# 產生模擬資料
X = np.linspace(0, 100, n_samples).reshape(-1, 1)
y = 3 * X.squeeze() + 7 + np.random.randn(n_samples) * noise

# 建立模型並擬合
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# 畫圖
fig, ax = plt.subplots()
ax.scatter(X, y, label="Data")
ax.plot(X, y_pred, color='red', label="Regression Line")
ax.legend()
st.pyplot(fig)
