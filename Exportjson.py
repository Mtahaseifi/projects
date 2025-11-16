import pandas as pd
import json
import re

def process_school_csv(file_path):
    # خواندن کل فایل
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    students_data = []
    
    # تقسیم بر اساس خطوط خالی (هر بخش یک کلاس)
    sections = content.strip().split('\n\n')
    
    for section in sections:
        if not section.strip():
            continue
            
        lines = [line.strip() for line in section.split('\n') if line.strip()]
        
        # پیدا کردن خط هدر
        header_line = None
        for line in lines:
            if 'ID,Name,Surname,nationalcode' in line:
                header_line = line
                break
        
        if not header_line:
            continue
            
        # تشخیص اینکه آیا این بخش دفاعی داره
        has_defensive = 'difensive' in header_line
        expected_columns = 20 if has_defensive else 19
        
        # پردازش خطوط داده
        for line in lines:
            # خطوطی که داده واقعی هستند (شامل عدد و کاما)
            if (line.strip() and 
                'ID,Name,Surname,nationalcode' not in line and 
                ',' in line and 
                any(char.isdigit() for char in line)):
                
                parts = [part.strip() for part in line.split(',')]
                
                # اگر تعداد ستون‌ها کمتر از حداقل مورد نیاز هست، skip کن
                if len(parts) < 19:
                    continue
                    
                try:
                    student = {
                        "student_id": parts[0],
                        "first_name": parts[1],
                        "last_name": parts[2],
                        "national_code": parts[3],
                        "art": parts[4],
                        "sport": parts[5],
                        "english": parts[6],
                        "technology": parts[7],
                        "social_studies": parts[8],
                        "writing": parts[9],
                        "dictation": parts[10],
                        "literature": parts[11],
                        "math": parts[12],
                        "science": parts[13],
                        "arabic": parts[14],
                        "thinking_lifestyle": parts[15],
                        "religious": parts[16],
                        "quran": parts[17]
                    }
                    
                    # مدیریت ستون plusone و defensive
                    if has_defensive and len(parts) >= 20:
                        student["defensive"] = parts[18]
                        student["plusone"] = parts[19]
                    elif len(parts) >= 19:
                        student["plusone"] = parts[18]
                    
                    students_data.append(student)
                    
                except Exception as e:
                    print(f"خطا در پردازش خط: {line}")
                    print(f"خطا: {e}")
                    continue
    
    return students_data

# اجرای برنامه
file_path = "nemat.csv"
students_data = process_school_csv(file_path)

# ذخیره در فایل JSON
with open('grades.json', 'w', encoding='utf-8') as f:
    json.dump({"students": students_data}, f, ensure_ascii=False, indent=2)

print(f"✅ فایل grades.json با موفقیت ایجاد شد")
print(f"📊 تعداد دانش آموزان پردازش شده: {len(students_data)}")

# نمایش نمونه داده‌ها
if students_data:
    print("\n📝 نمونه داده‌های پردازش شده:")
    for i, student in enumerate(students_data[:3]):  # نمایش 3 نمونه اول
        print(f"\nدانش آموز {i+1}:")
        print(f"  کد ملی: {student['national_code']}")
        print(f"  نام: {student['first_name']} {student['last_name']}")
        print(f"  دارای دفاعی: {'defensive' in student}")