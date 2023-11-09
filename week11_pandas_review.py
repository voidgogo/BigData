import pandas as pd

df = pd.DataFrame(
    [[99, 89, 81],
        [91, 98, 90],
        [95, 97, 85],
        [83, 96, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)

# def scale_score(n):
#     return n + 1
#
#
# print(df)
# df = df.apply(scale_score)
# print(df)

print(df)
df = df.apply(lambda n: n + 1)
print(df)