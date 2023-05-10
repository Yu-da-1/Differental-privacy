import numpy as np
import matplotlib.pyplot as plt

# データセットのサンプル
data = np.random.normal(0, 1, 1000)

# 真の平均値
true_mean = np.mean(data)

# Laplaceノイズを追加する関数
def add_laplace_noise(data, epsilon, sensitivity):
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale, len(data))
    return data + noise

# 差分プライバシーを適用してノイズ付きの平均値を計算
epsilon = 1000000000000000
sensitivity = 1.0
noisy_data = add_laplace_noise(data, epsilon, sensitivity)
noisy_mean = np.mean(noisy_data)

print(f"True mean: {true_mean}")
print(f"Noisy mean with differential privacy: {noisy_mean}")

# プロット
plt.hist(data, alpha=0.5, label="Original data")
plt.hist(noisy_data, alpha=0.5, label="Noisy data")
plt.legend(loc="upper right")
plt.show()
