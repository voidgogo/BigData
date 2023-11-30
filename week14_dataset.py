"""
1) 생존자와 사망자 수를 구하시오.
2) 남성과 여성의 생존률을 구하시오.
3) 객실 등급별 생존자 수를 구하시오.
4) 나이대별 생존자 수를 구하시오.

"""
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.head(10))

# [0, 10, 20, 30, 40, 50, 60 , 70, 80]
age_survived = titanic.groupby(pd.cut(titanic['age'], bins=range(0, 81, 10)))['survived'].sum()
print(age_survived)
