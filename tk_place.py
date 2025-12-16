import tkinter as tk

root = tk.Tk()
root.title("Tkinter Place")
root.geometry("400x300")
root.resizable(False, False)

# 左邊
left = tk.Frame(root, bg='lightgreen')
left.place(relx=0, rely=0, relwidth=0.1, relheight=1.0)

# 右邊
right = tk.Frame(root, bg='lightblue')
right.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)

# 上面紅色
top = tk.Frame(root, bg='red')
top.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)

# 中間黃色
middle = tk.Frame(root, bg='yellow')
middle.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

# 下面藍色
bottom = tk.Frame(root, bg='blue')
bottom.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.1)

# label
l1 = tk.Label(top, text='left', bg='white', fg='black')
l1.place(relx=0, rely=0, anchor='nw')

l2 = tk.Label(top, text='center', bg='white', fg='black')
l2.place(relx=0.33, rely=0, anchor='nw')

l3 = tk.Label(top, text='Right', bg='white', fg='black')
l3.place(relx=0.66, rely=0, anchor='nw')

root.mainloop()