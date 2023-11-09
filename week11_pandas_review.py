import pandas as pd

df = pd.DataFrame(
    [[99, 89, 100],
        [91, 98, 90],
        [100, 97, 85],
        [83, 100, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)
print(df)
# df_copy = df.iloc[:, [0, 2]]
# df_copy = df.loc[:, ['KOR', 'MAT']]
df_copy = df.loc[:, 'KOR':'MAT':2]
print(df_copy)

df = (pd.melt(df)
       .rename(columns={
        'variable': 'subject',
        'value': 'score'})
       .query('score >= 90')
       .sort_values('score', ascending=False)
       )
print(df)
print(df.iloc[:, [1]])
