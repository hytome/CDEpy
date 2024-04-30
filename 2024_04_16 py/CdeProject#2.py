import numpy as np

if __name__ == "__main__":
    size = 10**7  # 데이터 포인트 수
    data = [np.random.randint(0, 2) for i in range(size)]
    x = [0 if value == 0 else 5 for value in data]  # 기본 신호

    num_paths = 3  # 다이버시티 경로 수 (예: 3개의 안테나)
    scale = 1  # 레일리 분포의 스케일 파라미터
    combined_signal = np.zeros(size)

    for _ in range(num_paths):
        rayleigh_fading = np.random.rayleigh(scale, size)
        path_signal = x + rayleigh_fading  # 각 경로의 신호
        combined_signal += path_signal  # 신호 결합

    combined_signal /= num_paths  # 평균을 취하여 결합

    # 잡음 추가
    noise = np.random.normal(0, 1, size)
    r = combined_signal + noise

    # 복조
    y = [1 if value >= 2.5 else 0 for value in r]

    # 성능 체크
    check = [1 if data[i] == y[i] else 0 for i in range(size)]
    correct_bits = sum(check)
    error_rate = (size - correct_bits) / size
    print(f"에러 확률: {error_rate}")