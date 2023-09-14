import numpy as np
import random
import tkinter as tk  # Built in GUI
from tkinter import messagebox  # pop-up window


def click_button():
    try:
        n = int(en_number.get())
        l = [random.randint(1, 100) for i in range(n)]
        v = np.array(l, dtype='int16')
        lbl_result.config(text=v)
    except ValueError as err:
        # lbl_result.config(text=f"입력 값이 없습니다.\n{err}")
        messagebox.showerror('Error!', f"입력 값이 없습니다.\n{err}")


window = tk.Tk()
window.title('numpy gui version v0.9')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy array")
en_number = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# widget layout
lbl_result.grid(row=0, column=0, columnspan=2)
en_number.grid(row=1, column=0)
btn_click.grid(row=1, column=1)
# lbl_result.pack(side='right')
# en_number.pack(side='right')
# btn_click.pack(side='right')

window.mainloop()
