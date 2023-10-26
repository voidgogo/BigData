import pandas as pd
import numpy as np
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
})

print(df)
# 1
# df.fillna(df.mean(), inplace=True)
# print(df)

# 2
# for col in df.columns:
#     #print(col)
#     df[col] = np.where(pd.isnull(df[col]), np.mean(df[col]), df[col])
# print(df)

# 3
from sklearn.impute import SimpleImputer  # 결측값 전용 처리 클래스 활용
i = SimpleImputer(strategy='mean')  # median, most frequent
df = pd.DataFrame(i.fit_transform(df), columns=df.columns)
print(df)
