عالی! در اینجا کد تغییر یافته را می‌نویسم که هر بار داده‌ای در دیتابیس تغییر کند، به طور خودکار فایل JSON به روز می‌شود:

```python
import sqlite3 as sq
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import json
import time
import os

conn = sq.connect('Nokhbino.sqlite')
crs = conn.cursor()

# جداول با plusone به صورت TEXT
crs.execute('''
CREATE TABLE IF NOT EXISTS class701(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT, 
    nationalcode TEXT,       
    art TEXT, 
    sport TEXT,
    english TEXT,
    technology TEXT,
    socialstudies TEXT,
    writing TEXT,
    dictation TEXT,
    literature TEXT,
    math TEXT,
    science TEXT,
    arabic TEXT,
    thinkinglifestyle TEXT,
    religious TEXT,
    quran TEXT,
    plusone TEXT               
)
''')

# سایر جداول به همین صورت...
# [کد جداول دیگر مانند قبل]

conn.commit()

class ScoresProject:
    def __init__(self,root):
       self.root = root
       self.root.title(title)
       self.root.geometry(size)
       self.root.configure(bg='LIGHTBLUE')
       
       # مسیر پیشفرض برای ذخیره خودکار JSON
       self.auto_json_path = "students_auto_backup.json"

       btn701 = tk.Button(root,text='701',width=20,command=self.open_701_window,bg='LIGHTGREEN')
       btn701.pack(pady=10)

       btn702 = tk.Button(root,text='702',width=20,command=self.open_702_window,bg='LIGHTGREEN')
       btn702.pack(pady=10)

       btn703 = tk.Button(root,text='703',width=20,command=self.open_703_window,bg='LIGHTGREEN')
       btn703.pack(pady=10)

       btn704 = tk.Button(root,text='704',width=20,command=self.open_704_window,bg='LIGHTGREEN')
       btn704.pack(pady=10)

       btn801 = tk.Button(root,text='801',width=20,command=self.open_801_window,bg='LIGHTGREEN')
       btn801.pack(pady=10)

       btn802 = tk.Button(root,text='802',width=20,command=self.open_802_window,bg='LIGHTGREEN')
       btn802.pack(pady=10)

       btn901 = tk.Button(root,text='901',width=20,command=self.open_901_window,bg='LIGHTGREEN')
       btn901.pack(pady=10)

       # دکمه برای ذخیره دستی (اختیاری)
       export_json_btn = tk.Button(root,text='ذخیره دستی JSON',command=self.export_json,width=20,bg='LIGHTGREEN')
       export_json_btn.pack(pady=10)
       
       # ایجاد فایل JSON در ابتدا
       self.auto_export_json()

    def auto_export_json(self, filepath=None):
        """تابع برای ذخیره خودکار JSON"""
        if filepath is None:
            filepath = self.auto_json_path
            
        try:
            all_students = []
            
            # جمع‌آوری داده از تمام کلاس‌ها
            classes = ['class701', 'class702', 'class703', 'class704', 'class801', 'class802', 'class901']
            
            for class_name in classes:
                crs.execute(f'SELECT * FROM {class_name}')
                students = crs.fetchall()
                
                for student in students:
                    student_dict = {
                        "student_id": str(student[0]),
                        "first_name": student[1],
                        "last_name": student[2],
                        "national_code": str(student[3]),
                        "art": str(student[4]),
                        "sport": str(student[5]),
                        "english": str(student[6]),
                        "technology": str(student[7]),
                        "social_studies": str(student[8]),
                        "writing": str(student[9]),
                        "dictation": str(student[10]),
                        "literature": str(student[11]),
                        "math": str(student[12]),
                        "science": str(student[13]),
                        "arabic": str(student[14]),
                        "thinking_lifestyle": str(student[15]),
                        "religious": str(student[16]),
                        "quran": str(student[17]),
                    }
                    
                    # اضافه کردن defensive برای کلاس 901
                    if class_name == 'class901' and len(student) > 19:
                        student_dict["defensive"] = str(student[18])
                        student_dict["plusone"] = student[19]
                    else:
                        student_dict["plusone"] = student[18]
                    
                    all_students.append(student_dict)
            
            # ساختار JSON مطابق نمونه شما
            json_data = {
                "students": all_students
            }
            
            # ذخیره فایل JSON
            with open(filepath, 'w', encoding='utf-8') as jsonfile:
                json.dump(json_data, jsonfile, ensure_ascii=False, indent=2)
                
            print(f"✅ فایل JSON به طور خودکار به روز شد: {filepath}")
            
        except Exception as e:
            print(f"❌ خطا در ذخیره خودکار JSON: {e}")

    def get_descriptive_plusone(self, parent_window):
        """دریافت نمره مثبت یک به صورت توصیفی"""
        while True:
            plusone = simpledialog.askstring(
                'نمره مثبت یک', 
                'نمره مثبت یک را وارد کنید (عالی/خوب/قابل قبول/نیاز به بهبود):',
                parent=parent_window
            )
            if plusone is None:
                return None
            if plusone in ["عالی", "خوب", "قابل قبول", "نیاز به بهبود"]:
                return plusone
            else:
                messagebox.showerror('خطا', 'لطفا یکی از گزینه‌های معتبر وارد کنید: عالی، خوب، قابل قبول، نیاز به بهبود')

    def validate_grade(self, grade, subject_name, parent_window):
        """اعتبارسنجی نمره"""
        if grade is None:
            return None
        try:
            grade_str = str(grade)
            if grade_str.replace('.', '').isdigit() and 0 <= float(grade) <= 20:
                return grade_str
            else:
                messagebox.showerror('خطا', f'نمره {subject_name} باید بین 0 و 20 باشد', parent=parent_window)
                return None
        except ValueError:
            messagebox.showerror('خطا', f'نمره {subject_name} باید عددی باشد', parent=parent_window)
            return None

    def open_701_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 701")
        window.geometry("1200x400") 

        tree = ttk.Treeview(window, columns=("ID","Name",'Surname','nc' ,"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran',  'plusone'), show='headings')
        # [کد مربوط به treeview مانند قبل...]
        
        def load_data():
            for i in tree.get_children():
                tree.delete(i)
            crs.execute('SELECT * FROM class701')
            for row in crs.fetchall():
                tree.insert('','end',values=row) 

        load_data()

        def add_student():
            name = simpledialog.askstring('Input','نام دانش اموز را وارد کنید',parent=window)
            if not name:
                return
            surname = simpledialog.askstring('Input','نام خانوادگی دانش اموز را وارد کنید',parent=window)
            if not surname:
                return          
            nc = simpledialog.askstring('Input','کد ملی دانش اموز را وارد کنید',parent=window)
            if not nc or len(str(nc)) != 10:
                messagebox.showerror('خطا', 'کد ملی باید 10 رقمی باشد', parent=window)
                return
            
            # دریافت نمرات
            art_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی هنر دانش اموز را وارد کنید',parent=window), 'هنر', window)
            if art_score is None: return
            sport_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی ورزش دانش اموز را وارد کنید',parent=window), 'ورزش', window)
            if sport_score is None: return
            english_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی زبان دانش اموز را وارد کنید',parent=window), 'زبان', window)
            if english_score is None: return
            technology_score = self.validate_grade(simpledialog.askfloat('Input',' نمره ی کار و فناوری دانش اموز را وارد کنید',parent=window), 'کار و فناوری', window)
            if technology_score is None: return
            socialstudies_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی مطالعات اجتماعی دانش موز را وارد کنید',parent=window), 'مطالعات اجتماعی', window)
            if socialstudies_score is None: return
            writing_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی نگارش دانش اموز را وارد کنید',parent=window), 'نگارش', window)
            if writing_score is None: return
            dictation_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی املا دانش اموز را وارد کنید',parent=window), 'املا', window)
            if dictation_score is None: return
            literature_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی ادبیات فارسی دانش اموز را وارد کنید',parent=window), 'ادبیات فارسی', window)
            if literature_score is None: return
            math_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی ریاضی دانش اموز را وارد کنید',parent=window), 'ریاضی', window)
            if math_score is None: return
            science_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی علوم دانش اموز را وارد کنید',parent=window), 'علوم', window)
            if science_score is None: return
            arabic_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی عربی دانش اموز را وارد کنید',parent=window), 'عربی', window)
            if arabic_score is None: return
            thinklifestyle_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی تفکر و سبک زندگی دانش اموز را وارد کنید',parent=window), 'تفکر و سبک زندگی', window)
            if thinklifestyle_score is None: return
            religious_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی دینی دانش اموز را وارد کنید',parent=window), 'دینی', window)
            if religious_score is None: return
            quran_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی قران دانش اموز را وارد کنید',parent=window), 'قران', window)
            if quran_score is None: return
            
            # دریافت نمره مثبت یک به صورت توصیفی
            plusone_score = self.get_descriptive_plusone(window)
            if plusone_score is None:
                return

            crs.execute('INSERT INTO class701 (name,surname,nationalcode,art,sport,english,technology,socialstudies,writing,dictation,literature,math,science,arabic,thinkinglifestyle,religious,quran,plusone) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (name,surname,nc,art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,literature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score))
            conn.commit()
            load_data()
            
            # 🔄 به روز رسانی خودکار JSON پس از اضافه کردن دانش‌آموز
            self.auto_export_json()

        def update_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return
            item = tree.item(selected[0])
            cid,*alll = item['values']
            name = simpledialog.askstring("Input", "نام جدید را وارد کنید : ", parent=window)
            if not name:
                return
            surname = simpledialog.askstring("Input", "نام خانوادگی جدید را وارد کنید",  parent=window)
            if not surname:
                return
            nc = simpledialog.askstring('Input','کد ملی دانش اموز را وارد کنید :',parent=window)
            if not nc or len(str(nc)) != 10:
                messagebox.showerror('خطا', 'کد ملی باید 10 رقمی باشد', parent=window)
                return
            crs.execute("UPDATE class701 SET name=?, surname=?,nationalcode=? WHERE id=?", (name, surname,nc, cid))
            conn.commit()
            load_data()
            
            # 🔄 به روز رسانی خودکار JSON پس از ویرایش
            self.auto_export_json()

        def update_scores():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return 
            
            item = tree.item(selected[0])
            cid,*alll = item['values']

            # دریافت نمرات
            art_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی هنر دانش اموز را وارد کنید',parent=window), 'هنر', window)
            if art_score is None: return
            sport_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی ورزش دانش اموز را وارد کنید',parent=window), 'ورزش', window)
            if sport_score is None: return
            english_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی زبان دانش اموز را وارد کنید',parent=window), 'زبان', window)
            if english_score is None: return
            technology_score = self.validate_grade(simpledialog.askfloat('Input',' نمره ی کار و فناوری دانش اموز را وارد کنید',parent=window), 'کار و فناوری', window)
            if technology_score is None: return
            socialstudies_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی مطالعات اجتماعی دانش موز را وارد کنید',parent=window), 'مطالعات اجتماعی', window)
            if socialstudies_score is None: return
            writing_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی نگارش دانش اموز را وارد کنید',parent=window), 'نگارش', window)
            if writing_score is None: return
            dictation_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی املا دانش اموز را وارد کنید',parent=window), 'املا', window)
            if dictation_score is None: return
            literature_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی ادبیات فارسی دانش اموز را وارد کنید',parent=window), 'ادبیات فارسی', window)
            if literature_score is None: return
            math_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی ریاضی دانش اموز را وارد کنید',parent=window), 'ریاضی', window)
            if math_score is None: return
            science_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی علوم دانش اموز را وارد کنید',parent=window), 'علوم', window)
            if science_score is None: return
            arabic_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی عربی دانش اموز را وارد کنید',parent=window), 'عربی', window)
            if arabic_score is None: return
            thinklifestyle_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی تفکر و سبک زندگی دانش اموز را وارد کنید',parent=window), 'تفکر و سبک زندگی', window)
            if thinklifestyle_score is None: return
            religious_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی دینی دانش اموز را وارد کنید',parent=window), 'دینی', window)
            if religious_score is None: return
            quran_score = self.validate_grade(simpledialog.askfloat('Input','نمره ی قران دانش اموز را وارد کنید',parent=window), 'قران', window)
            if quran_score is None: return
            
            # دریافت نمره مثبت یک به صورت توصیفی
            plusone_score = self.get_descriptive_plusone(window)
            if plusone_score is None:
                return

            crs.execute('UPDATE class701 SET  art=?,sport=?,english=?,technology=?,socialstudies=?,writing=?,dictation=?,literature=?,math=?,science=?,arabic=?,thinkinglifestyle=?,religious=?,quran=?,plusone=? WHERE id=?',
                       (art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,literature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score,cid))
            conn.commit()
            load_data()  
            
            # 🔄 به روز رسانی خودکار JSON پس از ویرایش نمرات
            self.auto_export_json()

        def delete_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning("خطا", "یک دانش اموز را انتخاب کنید تا حذف شود")
                return
            item = tree.item(selected[0])
            cid = item['values'][0]
            if messagebox.askyesno("Confirm", 'ایا از حذف این دانش اموز اطمینان دارید؟'):
                crs.execute("DELETE FROM class701 WHERE id=?", (cid,))
                conn.commit()
                load_data()    
                
                # 🔄 به روز رسانی خودکار JSON پس از حذف
                self.auto_export_json()

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ",command=add_student ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش نام و نام خانوادگی و کد ملی",command=update_student ).pack(side='left', padx=5)
        tk.Button(frame_buttons,text="ویرایش نمرات",command=update_scores).pack(side='left',padx=5)
        tk.Button(frame_buttons,text="حذف دانش اموز",command=delete_student).pack(side='left',padx=5)

    # سایر توابع open_window نیز باید به همین صورت تغییر کنند
    # (در هر تابع add_student, update_student, update_scores, delete_student)
    # باید self.auto_export_json() اضافه شود

    def export_json(self):
        """ذخیره دستی JSON (با انتخاب مسیر توسط کاربر)"""
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="ذخیره فایل JSON"
        )
        
        if filepath:
            self.auto_export_json(filepath)
            messagebox.showinfo("موفقیت", f"فایل JSON در مسیر مورد نظر ذخیره شد:\n{filepath}")

title = 'مدیریت نمرات مدرسه نخبینو'
size = '450x400'

root = tk.Tk()
project = ScoresProject(root)
root.mainloop()
```

مهم‌ترین تغییرات برای ذخیره خودکار:

1. auto_export_json() - تابع جدید برای ذخیره خودکار
2. self.auto_json_path - مسیر پیشفرض برای فایل JSON
3. فراخوانی self.auto_export_json() بعد از هر عملیات:
   · بعد از add_student()
   · بعد از update_student()
   · بعد از update_scores()
   · بعد از delete_student()
4. فایل JSON به طور خودکار با نام students_auto_backup.json ایجاد می‌شود

نتیجه: هر بار که دانش‌آموزی اضافه، ویرایش یا حذف شود، فایل JSON به طور خودکار به روز می‌شود! 🔄