
import numpy as np
data = np.array([
    [1, 5, 9],
    [2, np.nan, 10],
    [np.nan, 7, 11],
    [4, 8, np.nan]
])
print(data)

means = np.nanmean(data, axis=0)  # 각 column의 평균 값들
for i in range(data.shape[1]):
    mask = np.isnan(data[:, i]) # True, False 값을 갖는 배열 생성
    data[mask, i] = means[i]
print(data)
