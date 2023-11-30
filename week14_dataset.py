import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
#print(titanic.describe())
#print(titanic.head(10))
#print(titanic.tail(10))

# 결측치 전처리
print(titanic['age'].fillna(titanic['age'].median(), inplace=True))
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')  # 카테고리 추가
titanic['deck'].fillna('Unknown', inplace=True)
titanic['embarked'].fillna('Unknown', inplace=True)
titanic['embark_town'].fillna('Unknown', inplace=True)
print(titanic.info())
