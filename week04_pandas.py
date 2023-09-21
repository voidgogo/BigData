import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# csv file download and data loading
life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
# print(life_satisfaction.tail(5))
# print(life_satisfaction.shape)
# print(life_satisfaction.describe())
X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d array
y = life_satisfaction[["Life satisfaction"]].values  # return 2d array
# print(X)
# print(y)

# draw scatter diagram
life_satisfaction.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23500, 62500, 4, 9])
plt.show()

# model choice
model = LinearRegression()

# model train
model.fit(X, y)

# predict new GDP per capita (South Korea 2020)
X_new = [[31700]]
print(life_satisfaction)
print(model.predict(X_new))
