import tkinter as tk

root = tk.Tk()
root.title("Tkinter Grid")
root.geometry("400x300")
root.resizable(False, False)

# 設定格子
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, minsize=40)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, minsize=40)

# 左邊
left = tk.Frame(root, bg='lightgreen', width=40)
left.grid(row=0, column=0, rowspan=3, sticky='nsew')

# 右邊
right = tk.Frame(root, bg='lightblue', width=40)
right.grid(row=0, column=2, rowspan=3, sticky='nsew')

# 上面紅色
top = tk.Frame(root, bg='red', height=60)
top.grid(row=0, column=1, sticky='ew')
top.grid_propagate(False)

# 中間黃色
middle = tk.Frame(root, bg='yellow')
middle.grid(row=1, column=1, sticky='nsew')

# 下面藍色
bottom = tk.Frame(root, bg='blue', height=30)
bottom.grid(row=2, column=1, sticky='ew')
bottom.grid_propagate(False)

# label
l1 = tk.Label(top, text='left', bg='white', fg='black')
l1.pack(side='left', anchor='n')

l2 = tk.Label(top, text='center', bg='white', fg='black')
l2.pack(side='left', anchor='n')

l3 = tk.Label(top, text='Right', bg='white', fg='black')
l3.pack(side='left', anchor='n')

root.mainloop()