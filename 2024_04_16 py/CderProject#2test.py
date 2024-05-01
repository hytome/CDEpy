import numpy as np

def transmit(data, noise_std):
    """ 데이터 전송 및 잡음 추가 """
    x = [5 if value == 1 else 0 for value in data]
    n = np.random.randn(len(data)) * noise_std
    r = np.array(x) + n
    y = [1 if value >= 2.5 else 0 for value in r]
    return y

def receive(data, transmitted_data):
    """ 데이터 수신 및 에러 체크 """
    errors = [i for i, (original, received) in enumerate(zip(data, transmitted_data)) if original != received]
    return errors

def automatic_repeat_request(data, noise_std, max_retries=10):
    """ ARQ 프로토콜 구현 """
    retries = 0
    transmitted_data = transmit(data, noise_std)
    errors = receive(data, transmitted_data)
    
    while errors and retries < max_retries:
        print(f"재전송 횟수: {retries+1}, 에러 위치 수: {len(errors)}")
        for error_index in errors:
            data[error_index] = data[error_index]  # 재전송을 위해 에러 위치의 데이터를 다시 설정
        transmitted_data = transmit(data, noise_std)
        errors = receive(data, transmitted_data)
        retries += 1
    
    return transmitted_data, retries

# 데이터 생성
data = np.random.randint(0, 2, 1000)  # 1000개의 비트

# ARQ 시뮬레이션 실행
final_data, total_retries = automatic_repeat_request(data, noise_std=1.0)
print(f"총 재전송 횟수: {total_retries}")