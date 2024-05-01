import numpy as np

def transmit(data, noise_std):
    """ 데이터 전송 및 잡음 추가 """
    x = [5 if value == 1 else 0 for value in data]
    n = np.random.randn(len(data)) * noise_std
    r = np.array(x) + n
    y = [1 if value >= 2.5 else 0 for value in r]
    
    return x, n, r, y

def print_arrays(data, x, n, r, y):
    """ 배열 출력 """
    print("data의 배열 (첫 30개):", data[:30])
    print("배열 x의 값 (첫 30개):", x[:30])
    print("배열 n의 값 (첫 30개, 소수점 4자리):", np.round(n[:30], 4))
    print("배열 r의 값 (첫 30개, 소수점 4자리):", np.round(r[:30], 4))
    print("배열 y의 값 (첫 30개):", y[:30])

def receive(data, transmitted_data):
    """ 데이터 수신 및 에러 체크 """
    errors = [i for i, (original, received) in enumerate(zip(data, transmitted_data)) if original != received]
    return errors

def automatic_repeat_request(data, noise_std, max_retries=10):
    """ ARQ 프로토콜 구현 """
    retries = 0
    x, n, r, transmitted_data = transmit(data, noise_std)
    errors = receive(data, transmitted_data)
    
    while errors and retries < max_retries:
        print(f"재전송 횟수: {retries+1}, 에러 위치 수: {len(errors)}")
        for error_index in errors:
            _, _, _, transmitted_data[error_index] = transmit([data[error_index]], noise_std)
        errors = receive(data, transmitted_data)
        retries += 1
    
    return transmitted_data, retries

# 데이터 생성 (크기를 줄여 테스트)
data = np.random.randint(0, 2, 10**7)  # 10의 7승개.

# 먼저 배열 출력
x, n, r, y = transmit(data, 1.0)
print_arrays(data, x, n, r, y)

# ARQ 시뮬레이션 실행
final_data, total_retries = automatic_repeat_request(data, noise_std=1.0)
print(f"총 재전송 횟수: {total_retries}")

# 최종 결과 확인
correct_bits = sum(1 for i in range(len(data)) if data[i] == final_data[i])
error_bits = len(data) - correct_bits
error_probability = error_bits / len(data)
print("수신기가 바르게 복원한 비트의 개수:", correct_bits)
print("수신기의 에러 확률 (ρ):", error_probability)