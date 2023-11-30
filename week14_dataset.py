"""
1) 생존자와 사망자 수를 구하시오.
2) 남성과 여성의 생존률을 구하시오.
3) 객실 등급별 생존자 수를 구하시오.
4) 나이대별 생존자 수를 구하시오.
5) 생존자와 사망자의 나이 분포를 시각화해보시오.

"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.head(10))
survived_ages = titanic[titanic['survived'] == 1]['age'].dropna()
dead_ages = titanic[titanic['survived'] == 0]['age'].dropna()

plt.hist(survived_ages, bins=20, label='Survived', alpha=0.5)
plt.hist(dead_ages, bins=20, label='Dead', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.show()