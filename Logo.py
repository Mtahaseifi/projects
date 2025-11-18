import tkinter as tk
from PIL import Image, ImageTk  # نیاز به نصب pillow: pip install pillow

root = tk.Tk()
root.title("پس‌زمینه با لوگو")
root.geometry("800x600")

# بارگذاری تصویر
try:
    # روش 1: با PIL (توصیه شده)
    image = Image.open("logo.png")  # مسیر تصویر لوگو
    background_image = ImageTk.PhotoImage(image)
    
    # روش 2: بدون PIL (فقط برای فرمت GIF/PGM/PPM)
    # background_image = tk.PhotoImage(file="logo.gif")
    
except Exception as e:
    print(f"خطا در بارگذاری تصویر: {e}")
    root.destroy()

# ایجاد Label برای نمایش تصویر پس‌زمینه
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # پر کردن کل پنجره

# اضافه کردن ویجت‌های دیگر روی تصویر
title_label = tk.Label(root, text="عنوان برنامه", font=("Arial", 20), bg="white")
title_label.pack(pady=20)

button = tk.Button(root, text="دکمه نمونه", font=("Arial", 14))
button.pack(pady=10)

root.mainloop()