import numpy as np

# 0과 1을 랜덤으로 10의 7승 개 생성하여 'data' 배열에 저장
data = np.random.randint(0, 2, 10**7)

# 'data' 배열의 첫 30개 값 출력
print("data")
print(data[:30])

x = [5 if value == 1 else 0 for value in data]

# 'x' 배열의 첫 30개 값 출력
print("x")
print(x[:30])

# 평균이 0이고 표준 편차가 1인 Gaussian 분포를 따르는 잡음을 10의 7승 개 생성
n = np.random.randn(10**7)

# 'n' 배열의 첫 30개 값 출력, 소수점 아래 4자리까지
print("noise")
print(np.round(n[:30], 4))
r = x + n

# 'r' 배열의 첫 30개 값 출력, 소수점 아래 4자리까지
print("r")
print(np.round(r[:30], 4))

y = [1 if value >= 2.5 else 0 for value in r]

# 'y' 배열의 첫 30개 값 출력
print("y")
print(y[:30])

check = [1 if data[i] == y[i] else 0 for i in range(len(data))]
print("check의 첫 30개 값:")
print(check[:30])

correct_bits = sum(check)
print("수신기가 바르게 복원한 비트의 개수:")
print(correct_bits)

error_bits = len(data) - correct_bits
error_probability = error_bits / len(data)
print("수신기의 에러 확률 (ρ):")
print(error_probability)

error_rate = []

# 잡음의 표준 편차를 0에서 2.9까지 0.1 간격으로 변경하면서 에러 확률 계산
for std_dev in np.arange(0, 3.0, 0.1):
    n = np.random.randn(10**7) * std_dev
    r = x + n
    y = [1 if value >= 2.5 else 0 for value in r]
    check = [1 if data[i] == y[i] else 0 for i in range(len(data))]
    correct_bits = sum(check)
    error_bits = len(data) - correct_bits
    error_probability = error_bits / len(data)
    error_rate.append(error_probability)

# 에러 확률을 소수점 아래 6자리까지 출력
print("표준 편차 | 에러 확률")
for i, rate in enumerate(error_rate):
    print(f"{i*0.1:.1f}      | {rate:.6f}")