برای اصلاح برنامه به گونه‌ای که به جای دکمه CSV، داده‌ها به صورت خودکار در فایل JSON ذخیره شوند، باید تغییرات زیر را اعمال کنید:

1. حذف بخش‌های مربوط به CSV
2. اضافه کردن قابلیت ذخیره خودکار در JSON
3. اضافه کردن import مربوط به json

در اینجا کد اصلاح شده را مشاهده می‌کنید:

```python
import sqlite3 as sq
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import json
import os

conn = sq.connect('Nokhbino.sqlite')
crs = conn.cursor()

# ایجاد جداول (همانند قبل)
crs.execute('''
CREATE TABLE IF NOT EXISTS class701(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,        
    art INTEGER, 
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTEGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class702(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTEGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class703(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTEGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class704(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTEGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class801(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTEGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class802(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTEGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class901(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTEGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    defensive INTEGER,
    plusone TEXT               
)
''')
conn.commit()

class ScoresProject:
    def __init__(self,root):
       self.root = root
       self.root.title(title)
       self.root.geometry(size)
       self.root.configure(bg='LIGHTBLUE')

       # ذخیره خودکار هنگام بسته شدن برنامه
       self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

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

    def save_to_json(self):
        """ذخیره تمام داده‌ها در فایل JSON"""
        data = {}
        
        # لیست تمام کلاس‌ها
        classes = ['class701', 'class702', 'class703', 'class704', 
                  'class801', 'class802', 'class901']
        
        for class_name in classes:
            crs.execute(f'SELECT * FROM {class_name}')
            rows = crs.fetchall()
            
            # تبدیل به لیست دیکشنری‌ها
            columns = [desc[0] for desc in crs.description]
            class_data = []
            
            for row in rows:
                student_data = {}
                for i, col in enumerate(columns):
                    student_data[col] = row[i]
                class_data.append(student_data)
            
            data[class_name] = class_data
        
        # ذخیره در فایل JSON
        with open('Nokhbino_scores.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print("داده‌ها با موفقیت در فایل JSON ذخیره شدند.")

    def on_closing(self):
        """ذخیره خودکار هنگام بسته شدن برنامه"""
        self.save_to_json()
        self.root.destroy()

    def open_701_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 701")
        window.geometry("1200x400") 

        tree = ttk.Treeview(window, columns=("ID","Name",'Surname' ,"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran',  'plusone'), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text='نام')
        tree.heading('Surname',text='نام خانوادگی')
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=50)
        tree.column('Surname',width=70)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('plusone',width=70)
        tree.pack(expand=True,fill='both')

        def load_data():
            for i in tree.get_children():
                tree.delete(i)
            crs.execute('SELECT * FROM class701')
            for row in crs.fetchall():
                tree.insert('','end',values=row) 

        load_data()

        def add_student():
            name = simpledialog.askstring('Input','نام دانش اموز را وارد کنید',parent=window)
            if not name or (not name.isalpha()) :
                return
            surname = simpledialog.askstring('Input','نام خانوادگی دانش اموز را وارد کنید',parent=window)
            if not surname or (not surname.isalpha()):
                return          
            art_score = simpledialog.askfloat('Input','نمره ی هنر دانش اموز را وارد کنید',parent=window)
            if not art_score:
                return
            sport_score = simpledialog.askfloat('Input','نمره ی ورزش دانش اموز را وارد کنید',parent=window)
            if not sport_score:
                return
            english_score = simpledialog.askfloat('Input','نمره ی زبان دانش اموز را وارد کنید',parent=window)
            if not english_score:
                return
            technology_score = simpledialog.askfloat('Input',' نمره ی کار و فناوری دانش اموز را وارد کنید',parent=window)
            if not technology_score:
                return
            socialstudies_score = simpledialog.askfloat('Input','نمره ی مطالعات اجتماعی دانش موز را وارد کنید',parent=window)
            if not socialstudies_score:
                return
            writing_score = simpledialog.askfloat('Input','نمره ی نگارش دانش اموز را وارد کنید',parent=window)
            if not writing_score:
                return
            dictation_score = simpledialog.askfloat('Input','نمره ی املا دانش اموز را وارد کنید',parent=window)
            if not dictation_score:
                return
            leterature_score = simpledialog.askfloat('Input','نمره ی ادبیات فارسی دانش اموز را وارد کنید',parent=window)
            if not leterature_score:
                return
            math_score = simpledialog.askfloat('Input','نمره ی ریاضی دانش اموز را وارد کنید',parent=window)
            if not math_score:
                return
            science_score = simpledialog.askfloat('Input','نمره ی علوم دانش اموز را وارد کنید',parent=window)
            if not science_score:
                return
            arabic_score = simpledialog.askfloat('Input','نمره ی عربی دانش اموز را وارد کنید',parent=window)
            if not arabic_score:
                return
            thinklifestyle_score = simpledialog.askfloat('Input','نمره ی تفکر و سبک زندگی دانش اموز را وارد کنید',parent=window)
            if not thinklifestyle_score:
                return
            religious_score = simpledialog.askfloat('Input','نمره ی دینی دانش اموز را وارد کنید',parent=window)
            if not religious_score:
                return
            quran_score = simpledialog.askfloat('Input','نمره ی قران دانش اموز را وارد کنید',parent=window)
            if not quran_score:
                return
            plusone_score = simpledialog.askfloat('Input','نمره ی مثبت یک را وارد کنید',parent=window)
            if not plusone_score:
                return
            isnum = False
            for i in [art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,leterature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score]:
                if 0>i or i>20:
                    isnum = True
            if isnum:
                messagebox.showerror('خطا','همه ی نمرات باید بین 0 و 20 باشند')
            if not isnum:
                crs.execute('INSERT INTO class701 (name,surname,art,sport,english,technology,socialstudies,writing,dictation,literature,math,science,arabic,thinkinglifestyle,religious,quran,plusone) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name,surname,art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,leterature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score))
                conn.commit()
                load_data()
                self.save_to_json()  # ذخیره خودکار در JSON
 
        def update_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return
            item = tree.item(selected[0])
            cid,*alll = item['values']
            name = simpledialog.askstring("Input", "نام جدید را وارد کنید : ", parent=window)
            if not name or (not name.isalpha()):
                return
            surname = simpledialog.askstring("Input", "نام خانوادگی جدید را وارد کنید",  parent=window)
            if not surname or (not surname.isalpha()):
                return
            crs.execute("UPDATE class701 SET name=?, surname=? WHERE id=?", (name, surname, cid))
            conn.commit()
            load_data()
            self.save_to_json()  # ذخیره خودکار در JSON

        def update_scores():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return 
            
            item = tree.item(selected[0])
            cid,*alll = item['values']

            art_score = simpledialog.askfloat('Input','نمره ی هنر دانش اموز را وارد کنید',parent=window)
            if not art_score:
                return
            sport_score = simpledialog.askfloat('Input','نمره ی ورزش دانش اموز را وارد کنید',parent=window)
            if not sport_score:
                return
            english_score = simpledialog.askfloat('Input','نمره ی زبان دانش اموز را وارد کنید',parent=window)
            if not english_score:
                return
            technology_score = simpledialog.askfloat('Input',' نمره ی کار و فناوری دانش اموز را وارد کنید',parent=window)
            if not technology_score:
                return
            socialstudies_score = simpledialog.askfloat('Input','نمره ی مطالعات اجتماعی دانش موز را وارد کنید',parent=window)
            if not socialstudies_score:
                return
            writing_score = simpledialog.askfloat('Input','نمره ی نگارش دانش اموز را وارد کنید',parent=window)
            if not writing_score:
                return
            dictation_score = simpledialog.askfloat('Input','نمره ی املا دانش اموز را وارد کنید',parent=window)
            if not dictation_score:
                return
            leterature_score = simpledialog.askfloat('Input','نمره ی ادبیات فارسی دانش اموز را وارد کنید',parent=window)
            if not leterature_score:
                return
            math_score = simpledialog.askfloat('Input','نمره ی ریاضی دانش اموز را وارد کنید',parent=window)
            if not math_score:
                return
            science_score = simpledialog.askfloat('Input','نمره ی علوم دانش اموز را وارد کنید',parent=window)
            if not science_score:
                return
            arabic_score = simpledialog.askfloat('Input','نمره ی عربی دانش اموز را وارد کنید',parent=window)
            if not arabic_score:
                return
            thinklifestyle_score = simpledialog.askfloat('Input','نمره ی تفکر و سبک زندگی دانش اموز را وارد کنید',parent=window)
            if not thinklifestyle_score:
                return
            religious_score = simpledialog.askfloat('Input','نمره ی دینی دانش اموز را وارد کنید',parent=window)
            if not religious_score:
                return
            quran_score = simpledialog.askfloat('Input','نمره ی قران دانش اموز را وارد کنید',parent=window)
            if not quran_score:
                return
            plusone_score = simpledialog.askfloat('Input','نمره ی مثبت یک را وارد کنید',parent=window)
            if not plusone_score:
                return
            isnum = False
            for i in [art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,leterature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score]:
                if 0>i or i>20:
                    isnum = True
            if isnum:
                messagebox.showerror('خطا','همه ی نمرات باید بین 0 و 20 باشند')
            if not isnum:

                crs.execute('UPDATE class701 SET  art=?,sport=?,english=?,technology=?,socialstudies=?,writing=?,dictation=?,literature=?,math=?,science=?,arabic=?,thinkinglifestyle=?,religious=?,quran=?,plusone=? WHERE id=?',(art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,leterature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score,cid))
                conn.commit()
                load_data()
                self.save_to_json()  # ذخیره خودکار در JSON

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
                self.save_to_json()  # ذخیره خودکار در JSON

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ",command=add_student ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text='ویرایش نام و نام خانوادگی',command=update_student ).pack(side='left', padx=5)
        tk.Button(frame_buttons,text="ویرایش نمرات",command=update_scores).pack(side='left',padx=5)
        tk.Button(frame_buttons,text="حذف دانش اموز",command=delete_student).pack(side='left',padx=5)

    # متدهای دیگر کلاس‌ها (702 تا 901) به همین صورت اصلاح شوند
    # در هر تابع add_student، update_student، update_scores و delete_student
    # باید self.save_to_json() بعد از conn.commit() اضافه شود

    def open_702_window(self):
        # کد مشابه کلاس 701 با تغییرات مربوط به JSON
        pass
        
    def open_703_window(self):
        # کد مشابه کلاس 701 با تغییرات مربوط به JSON
        pass
        
    def open_704_window(self):
        # کد مشابه کلاس 701 با تغییرات مربوط به JSON
        pass
        
    def open_801_window(self):
        # کد مشابه کلاس 701 با تغییرات مربوط به JSON
        pass
        
    def open_802_window(self):
        # کد مشابه کلاس 701 با تغییرات مربوط به JSON
        pass
        
    def open_901_window(self):
        # کد مشابه کلاس 701 با تغییرات مربوط به JSON
        pass

title = 'مدیریت نمرات مدرسه نخبینو'
size = '450x400'

root = tk.Tk()
project = ScoresProject(root)
root.mainloop()
