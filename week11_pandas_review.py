import pandas as pd

df1 = pd.DataFrame(
    {
        "KOR": [99, 91, 100],
        "ENG": [89, 98, 97],
        "MAT": [100, 90, 85],
    }, index=[1, 2, 3]
)
print(df1)

df2 = pd.DataFrame(
    [[99, 89, 100],
        [91, 98, 90],
        [100, 97, 85]],
    index=[1, 2, 3],
    columns=['KOR', 'ENG', 'MAT']
)
print(df2)