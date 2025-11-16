import pandas as pd
import json
import re

def process_school_csv(file_path):
    # خواندن کل فایل
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # تقسیم محتوا بر اساس "نمرات کلاس"
    classes = re.split(r'نمرات کلاس \d+:', content)
    
    students_data = []
    
    for i, class_section in enumerate(classes[1:], 1):
        if not class_section.strip():
            continue
            
        # پیدا کردن شماره کلاس
        class_match = re.findall(r'نمرات کلاس (\d+):', content)
        if class_match and i <= len(class_match):
            class_name = class_match[i-1]
        else:
            if i <= 4:
                class_name = f"70{i}"
            elif i <= 6:
                class_name = f"80{i-4}"
            else:
                class_name = f"90{i-6}"
        
        # تقسیم خطوط
        lines = [line.strip() for line in class_section.strip().split('\n') if line.strip()]
        
        # پیدا کردن خط هدر
        header_line = None
        for line in lines:
            if 'ایدی' in line and 'نام' in line:
                header_line = line
                break
        
        if not header_line:
            continue
            
        # تشخیص اینکه آیا کلاس 901 هست (ستون دفاعی داره)
        is_class_901 = 'دفاعی' in header_line
        
        # پردازش خطوط داده
        for line in lines:
            if line and 'ایدی' not in line and any(char.isdigit() for char in line):
                parts = [part.strip() for part in line.split(',')]
                if len(parts) >= 17:  # حداقل داده لازم
                    try:
                        student = {
                            "student_id": parts[0],
                            "first_name": parts[1],
                            "last_name": parts[2],
                            "national_code": f"0012345{parts[0].zfill(3)}",  # کد ملی نمونه
                            "class": class_name,
                            "art": parts[3],
                            "sport": parts[4],
                            "language": parts[5],
                            "technology": parts[6],
                            "social_studies": parts[7],
                            "writing": parts[8],
                            "spelling": parts[9],
                            "persian_literature": parts[10],
                            "math": parts[11],
                            "science": parts[12],
                            "arabic": parts[13],
                            "thinking": parts[14],
                            "religion": parts[15],
                            "quran": parts[16],
                            "positive": parts[17]
                        }
                        
                        # اگر کلاس 901 هست، ستون دفاعی رو اضافه کن
                        if is_class_901 and len(parts) >= 19:
                            student["defense"] = parts[18]
                        
                        students_data.append(student)
                        
                    except Exception as e:
                        print(f"خطا در پردازش خط: {line}")
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

# نمایش آمار کلاس‌ها
class_stats = {}
for student in students_data:
    class_name = student['class']
    if class_name not in class_stats:
        class_stats[class_name] = 0
    class_stats[class_name] += 1

print(f"🏫 آمار کلاس‌ها: {class_stats}")