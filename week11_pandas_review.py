import pandas as pd

df1 = pd.DataFrame(
    {
        "KOR": [99, 91, 100],
        "ENG": [89, 98, 97],
        "MAT": [100, 90, 85],
    }, index=[1, 2, 3]
)
print(df1)
print(df1.sort_values('MAT'))
df1 = df1.drop(columns=['ENG'])
print(df1)

df2 = pd.DataFrame(
    [[99, 89, 100],
        [91, 98, 90],
        [100, 97, 85]],
    index=[1, 2, 3],
    columns=['KOR', 'ENG', 'MAT']
)
print(df2)
df2 = (pd.melt(df2)
       .rename(columns={
        'variable': 'subject',
        'value': 'score'})
       .query('score >= 90')
       .sort_values('score', ascending=False)
       )

print(df2)


