import pandas as pd
import json

# خواندن فایل CSV
df = pd.read_csv('nemat.csv', encoding='utf-8')

# تبدیل به JSON
students_data = []
for _, row in df.iterrows():
    student = {
        "national_code": str(row['کد_ملی']),  # تغییر این خط
        "first_name": row['نام'],
        "last_name": row['نام خانوادگی'],
        "art": str(row['هنر']),
        "sport": str(row['ورزش']),
        "language": str(row['زبان']),
        "technology": str(row['کارو فناوری']),
        "social_studies": str(row['مطالعات اجتماعی']),
        "writing": str(row['نگارش']),
        "spelling": str(row['املا']),
        "persian_literature": str(row['ادبیات فارسی']),
        "math": str(row['ریاضی']),
        "science": str(row['علوم']),
        "arabic": str(row['عربی']),
        "thinking": str(row['تفکر و سبک زندگی']),
        "religion": str(row['دینی']),
        "quran": str(row['قران']),
        "positive": str(row['مثبت یک'])
    }
    
    # محاسبه معدل
    grade_columns = ['art', 'language', 'technology', 'social_studies', 
                    'writing', 'spelling', 'persian_literature', 'math', 
                    'science', 'arabic', 'thinking', 'religion', 'quran']
    
    grades = []
    for col in grade_columns:
        try:
            grade = float(row[col])
            if grade > 0:
                grades.append(grade)
        except:
            continue
    
    if grades:
        student['average'] = round(sum(grades) / len(grades), 2)
    else:
        student['average'] = 0
    
    students_data.append(student)

# ذخیره در فایل JSON
with open('grades.json', 'w', encoding='utf-8') as f:
    json.dump({"students": students_data}, f, ensure_ascii=False, indent=2)

print("✅ فایل grades.json با کد ملی ایجاد شد")