import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("TreeView با یک تصویر")
root.geometry("400x300")

# ایجاد TreeView
tree = ttk.Treeview(root, columns=("name", "age"), show="tree headings")
tree.heading("#0", text="آیتم")
tree.heading("name", text="نام")
tree.heading("age", text="سن")

# بارگذاری یک تصویر JPG
try:
    # مسیر عکس خودت رو اینجا بذار
    img = Image.open("photo.jpg")  # جایگزین کن با مسیر واقعی عکس
    img = img.resize((30, 30), Image.Resampling.LANCZOS)
    my_image = ImageTk.PhotoImage(img)
except:
    # اگر عکس پیدا نشد، یک عکس قرمز بساز
    img = Image.new('RGB', (30, 30), color='red')
    my_image = ImageTk.PhotoImage(img)

# اضافه کردن داده به TreeView با یک عکس
tree.insert("", "end", text="کاربر ۱", values=("علی", "25"), image=my_image)
tree.insert("", "end", text="کاربر ۲", values=("فاطمه", "30"), image=my_image)
tree.insert("", "end", text="کاربر ۳", values=("رضا", "28"), image=my_image)

# نمایش TreeView
tree.pack(expand=True, fill="both", padx=10, pady=10)

# اجرای برنامه
root.mainloop()