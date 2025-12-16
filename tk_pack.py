import tkinter as tk

root = tk.Tk()
root.title("Tkinter Pack")
root.geometry("400x300")
root.resizable(False, False)

# 左邊綠色
left = tk.Frame(root, bg='lightgreen', width=40)
left.pack(side='left', fill='y')

# 右邊藍色
right = tk.Frame(root, bg='lightblue', width=40)
right.pack(side='right', fill='y')

# 中間
center = tk.Frame(root)
center.pack(side='left', fill='both', expand=True)

# 紅色上面
top = tk.Frame(center, bg='red', height=60)
top.pack(side='top', fill='x')
top.pack_propagate(False)

# 藍色下面
bottom = tk.Frame(center, bg='blue', height=30)
bottom.pack(side='bottom', fill='x')
bottom.pack_propagate(False)

# 黃色中間
middle = tk.Frame(center, bg='yellow')
middle.pack(side='top', fill='both', expand=True)

# 三個label
l1 = tk.Label(top, text='left', bg='white', fg='black')
l1.pack(side='left', anchor='n')

l2 = tk.Label(top, text='center', bg='white', fg='black')
l2.pack(side='left', anchor='n')

l3 = tk.Label(top, text='Right', bg='white', fg='black')
l3.pack(side='left', anchor='n')

root.mainloop()