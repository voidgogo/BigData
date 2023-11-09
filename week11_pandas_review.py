import pandas as pd

df = pd.DataFrame(
    [[99, 89, 81],
        [91, 98, 90],
        [95, 97, 85],
        [83, 96, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)
# 각 과목별 평균 출력
print(df.mean())
# 각 과목별 최우수 성적 출력
print(df.max())

print(df)
# 국어 성적과 영어 성적이 둘 다 95점 이상인 행을 추출
print(df.query('KOR>=95 and ENG>=95'))
# 1번 학생의 수학 성적(81) 출력
print(df.at[1, 'MAT'])
#print(df.iat[1, 3])  # error, 0행 0열 부터 시작한다. index기반 (label X)
print(df.iat[0, 2])
# 국어, 수학 칼럼을 추출
# 조건은 국어 성적이 95점 이상인 경우
df_copy = df.loc[df['KOR']>=95, ['KOR', 'MAT']]
print(df_copy)


def scale_score(n):
    return n + 1


df = df.apply(scale_score)
print(df)