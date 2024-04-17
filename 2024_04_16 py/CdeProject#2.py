

    # 0과 1로 이루어진 10의 7승 크기의 배열 생성

if __name__ == "__main__":
    import numpy as np
    size=10**4
    #나중에 7로 수정하기.
    data= [np.random.randint(0,2,)for i in range(size)]
    
    print("data")
    print(data[:30])
    print()
    x = [0 if value == 0 else 5 for value in data]
    
    print("x")
    print(x[:30])
    print()
    noise = [round(np.random.rand(), 4) for _ in range(size)] # 소수점 4자리까지 반올림
    print("noise")
    print(noise[:30])
    #노이즈 생성.
    r = [x_val + noise_val for x_val, noise_val in zip(x, noise)]
    
    print("r")
    print(r[:30])
    y = [1 if value > 2.5 else 0 for value in r]
    
    
    