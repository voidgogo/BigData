"""
1) 생존자와 사망자 수를 구하시오.
2) 남성과 여성의 생존률을 구하시오.
3) 객실 등급별 생존자 수를 구하시오.

"""
import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.head(10))
pclass_survived = titanic.groupby('pclass')['survived'].sum()
# feat. jm lee
# pclass_survived = titanic[titanic['survived'] == 1].groupby(['pclass']).size()
print(pclass_survived)


