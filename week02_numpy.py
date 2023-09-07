import numpy as np
import random
import tkinter as tk  # Built in GUI

def click_button():
    n = int(en_number.get())
    l = [random.randint(1, 100) for i in range(n)]
    v = np.array(l, dtype='int16')
    lbl_result.config(text=v)


window = tk.Tk()
window.title('numpy gui version v0.7')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy array")
en_number = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# widget layout
lbl_result.pack()
en_number.pack(fill='x')
btn_click.pack(fill='x')

window.mainloop()
# n = int(input("input number : "))
# l = [random.randint(1, 100) for i in range(n)]
# v = np.array(l, dtype='int16')
# print(v)

