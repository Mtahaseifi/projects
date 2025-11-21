import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("TreeView با تصویر")
root.geometry("400x300")

# ایجاد TreeView
tree = ttk.Treeview(root, columns=("name", "age"), show="tree headings")
tree.heading("#0", text="آیتم")
tree.heading("name", text="نام")
tree.heading("age", text="سن")

# ساخت تصاویر ساده
images = {}

# تصویر قرمز
img_red = Image.new('RGB', (20, 20), color='red')
images['red'] = ImageTk.PhotoImage(img_red)

# تصویر سبز
img_green = Image.new('RGB', (20, 20), color='green')
images['green'] = ImageTk.PhotoImage(img_green)

# تصویر آبی
img_blue = Image.new('RGB', (20, 20), color='blue')
images['blue'] = ImageTk.PhotoImage(img_blue)

# اضافه کردن داده به TreeView
# آیتم‌های اصلی
user1 = tree.insert("", "end", text="کاربر ۱", 
                   values=("علی", "25"),
                   image=images['red'])

user2 = tree.insert("", "end", text="کاربر ۲", 
                   values=("فاطمه", "30"),
                   image=images['green'])

user3 = tree.insert("", "end", text="کاربر ۳", 
                   values=("رضا", "28"),
                   image=images['blue'])

# اضافه کردن زیرآیتم‌ها
tree.insert(user1, "end", text="پروژه A", 
           values=("وب سایت", "2 ماه"),
           image=images['blue'])

tree.insert(user1, "end", text="پروژه B", 
           values=("اپلیکیشن", "3 ماه"),
           image=images['green'])

tree.insert(user2, "end", text="پروژه C", 
           values=("دیتابیس", "1 ماه"),
           image=images['red'])

# نمایش TreeView
tree.pack(expand=True, fill="both", padx=10, pady=10)

# اجرای برنامه
root.mainloop()