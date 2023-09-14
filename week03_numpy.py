import numpy as np
# import random
import tkinter as tk  # Built in GUI
from tkinter import messagebox  # pop-up window


def create_2d_array(row, col):
    """
    행과 열값을 입력 받아 2차원 넘파이 배열을 반환하는 함수
    :param row: 행
    :param col: 열
    :return: 넘파이 2차원 배열
    """
    return np.random.randint(1, 101, size=(row, col))


def click_button():
    try:
        r, c = map(int, en_row_column.get().split())  # spacebar
        # rows = [[random.randint(1, 100) for i in range(r)] for i in range(c)]
        # matrix = np.array(create_2d_array(r, c), dtype='int16')
        matrix = create_2d_array(r, c)
        lbl_result.config(text=matrix)
    except ValueError as err:
        lbl_result.config(text=f"입력 값이 없습니다.\n{err}")
        messagebox.showerror('Error!', f"입력 값이 없습니다.\n{err}")


window = tk.Tk()
window.title('numpy gui version v1.5')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy 2d array")
en_row_column = tk.Entry()
#en_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# widget layout
# lbl_result.grid(row=0, column=0, columnspan=2)
# en_row.grid(row=1, column=0)
# en_column.grid(row=1, column=1)
# btn_click.grid(row=2, column=0, columnspan=2, sticky=tk.EW)
lbl_result.pack()
en_row_column.pack(fill='x')
btn_click.pack(fill='x')

window.mainloop()
