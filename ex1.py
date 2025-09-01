import numpy as np
import matplotlib.pyplot as plt

# 가상의 데이터 (예시)
np.random.seed(42)
actual_age = np.random.randint(20, 80, 50)  # 실제 나이
# 메틸화 기반 예측 나이 = 실제 나이 + 오차
predicted_age = actual_age + np.random.normal(0, 5, 50)

plt.figure(figsize=(6,6))
plt.scatter(actual_age, predicted_age, alpha=0.7)
plt.plot([20,80], [20,80], 'r--', label="y=x (예측=실제)")
plt.xlabel("실제 나이 (Chronological Age)")
plt.ylabel("예측 나이 (Epigenetic Age)")
plt.title("DNA 메틸화 기반 생물학적 나이 예측")
plt.legend()
plt.show()

