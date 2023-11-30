"""
1) 생존자와 사망자 수를 구하시오.
2) 남성과 여성의 생존률을 구하시오.

"""
import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.head())
male_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'male')]['survived'].count()
female_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'female')]['survived'].count()
male_count = titanic[(titanic['sex'] == 'male')]['sex'].count()
female_count = titanic[(titanic['sex'] == 'female')]['sex'].count()
print(male_survived, male_count, female_survived, female_count)
print(male_survived/male_count, female_survived/female_count)



