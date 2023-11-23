import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

print(titanic.isnull().sum())
print(titanic['age'].fillna(titanic['age'].median(), inplace=True))
print(titanic.isnull().sum())
# titanic['deck'].fillna('Unknown', inplace=True)  # 범주형 카테고리에 Unknown이 없음
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')  # 카테고리 추가
titanic['deck'].fillna('Unknown', inplace=True)

# print(type(titanic))
# print(titanic.describe())
# print(titanic.info())
# print(titanic.tail())
print(titanic['deck'].tail(10))