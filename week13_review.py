import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

print(titanic.isnull())

# print(type(titanic))
# print(titanic.describe())
# print(titanic.info())
# print(titanic)