# 在 Python 中，Tkinter 是一个非常流行的 GUI 库，可以用于构建桌面应用程序。要创建弹出式菜单（通常称为右键菜单或上下文菜单），可以使用 tkinter.Menu 和绑定鼠标事件来实现
# 如果没有安卓tkinter , python -m tkinter
import tkinter as tk

def on_open():
    print("打开文件...")

def on_save():
    print("保存文件...")

def on_exit():
    print("退出程序...")
    root.quit()

def show_popup_menu(event):
    popup_menu.post(event.x_root, event.y_root)

root = tk.Tk()
root.title("Tkinter 弹出菜单示例")
root.geometry("300x200")

# 绑定右键点击事件
root.bind("<Button-3>", show_popup_menu)

# 创建一个右键点击的菜单
popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="打开", command=on_open)
popup_menu.add_command(label="保存", command=on_save)
popup_menu.add_command(label="打开 ctrl o", command=on_open, accelerator="Ctrl+O")
popup_menu.add_separator()  # 添加分隔符
popup_menu.add_command(label="退出", command=on_exit)


root.mainloop() #Tkinter 会一直运行一个事件循环（mainloop()），等待并响应用户的操作。当 mainloop() 被启动时，它进入事件循环，不断检测事件队列。
# 在 Tkinter 中，事件（即消息）是由用户交互（如鼠标点击、键盘按键）或系统事件（如窗口大小变化、焦点变化等）自动触发的。
# 程序员并不需要手动发送这些事件，而是通过 bind()、bind_all() 等方法将事件和回调函数绑定起来，确保在事件发生时调用相关的处理函数。



