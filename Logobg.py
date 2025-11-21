import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("TreeView با پس زمینه عکس")
root.geometry("600x400")

# ایجاد فریم برای TreeView
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

# بارگذاری عکس برای پس زمینه
try:
    bg_image = Image.open("logo.jpg")  # نام عکس لوگو خودت را اینجا بگذار
    bg_photo = ImageTk.PhotoImage(bg_image)
except:
    bg_photo = None

# ایجاد TreeView
tree = ttk.Treeview(frame, columns=("name", "value"), show="tree headings")
tree.heading("#0", text="آیتم")
tree.heading("name", text="نام")
tree.heading("value", text="مقدار")

# اگر عکس موجود بود، ستایش به عنوان پس زمینه
if bg_photo:
    # ایجاد لیبل برای پس زمینه
    bg_label = tk.Label(frame, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # قرار دادن TreeView در جلوی عکس
    tree.pack(expand=True, fill="both")

# اضافه کردن داده به TreeView
for i in range(10):
    tree.insert("", "end", text=f"آیتم {i+1}", values=(f"نام {i+1}", f"مقدار {i+1}"))

# اگر میخواهی عکس را در خود TreeView داشته باشی:
class TreeWithBackground(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_image = bg_photo
        
    def paint_bg(self):
        if self.bg_image:
            self._bg_label = tk.Label(self, image=self.bg_image)
            self._bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# اجرای برنامه
root.mainloop()