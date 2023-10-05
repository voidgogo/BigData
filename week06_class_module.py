import pandas as pd
import tkinter as tk
import tglearn


def predict_life_satisfaction():
    x = int(en_GDP_per_capita.get())  # scalar input
    X_new = [[x]]

    life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
    X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d array
    y = life_satisfaction[["Life satisfaction"]].values  # return 2d array

    model = tglearn.LinearRegression()
    model.fit(X, y)

    # predict new GDP per capita (South Korea 2020)
    lbl_life_satisfaction.config(text=f"해당 국가의 삶의 만족도는 {model.predict(X_new)}로 예상합니다.")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("삶의 만족도 예측 프로그램 v0.2")
    window.geometry("400x150")

    lbl_life_satisfaction = tk.Label(window, text="아래 입력상자에 삶의 만족도를 알고 싶은\n국가의 1인당 GDP값을 입력해주세요")
    en_GDP_per_capita = tk.Entry(window)
    btn_predict = tk.Button(window, text="예측", command=predict_life_satisfaction)

    lbl_life_satisfaction.pack()
    en_GDP_per_capita.pack(fill='x')
    btn_predict.pack(fill='x')

    window.mainloop()