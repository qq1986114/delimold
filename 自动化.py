import tkinter as tk
import subprocess

def open_calculator():
    subprocess.Popen('C:\Windows\system32\calc.exe')

# 创建窗口
window = tk.Tk()
window.title('自动打开计算器')

# 创建按钮
button = tk.Button(window, text='打开计算器', command=open_calculator)
button.pack(padx=50, pady=20)

# 运行窗口
window.mainloop()
