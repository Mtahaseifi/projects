<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سامانه نمرات تحصیلی - مدرسه نمونه</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Tahoma', 'Arial', sans-serif;
            text-align: center;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            direction: rtl;
        }
        
        .header {
            color: white;
            margin-bottom: 30px;
            padding: 20px;
        }
        
        .header h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 30px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        h2 {
            color: #333;
            margin-bottom: 25px;
            font-size: 1.6em;
        }
        
        input {
            width: 100%;
            max-width: 400px;
            padding: 15px;
            margin: 15px 0;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            text-align: center;
        }
        
        button {
            background: #4CAF50;
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            margin: 15px 0;
            transition: all 0.3s;
        }
        
        button:hover {
            background: #45a049;
            transform: translateY(-2px);
        }
        
        .grade-card {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            margin: 25px 0;
            border: 2px solid #e9ecef;
        }
        
        .student-info {
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 8px;
            overflow: hidden;
        }
        
        th, td {
            padding: 12px 8px;
            border: 1px solid #dee2e6;
            text-align: center;
        }
        
        th {
            background: #667eea;
            color: white;
        }
        
        tr:nth-child(even) {
            background: #f8f9fa;
        }
        
        .class-badge {
            background: #ff6b6b;
            color: white;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 14px;
            margin: 0 10px;
        }
        
        .error-message {
            background: #ffebee;
            color: #c62828;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-right: 4px solid #c62828;
        }
        
        @media (max-width: 768px) {
            .container {
                margin: 10px;
                padding: 20px;
            }
            
            table {
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎓 سامانه نمرات تحصیلی</h1>
        <p>مدرسه نمونه</p>
    </div>

    <div class="container">
        <h2>مشاهده نمرات با کد ملی</h2>
        
        <input type="text" id="nationalCode" placeholder="کد ملی خود را وارد کنید" maxlength="10">
        <br>
        <button onclick="getGrades()">🔍 مشاهده نمرات</button>
        
        <div id="result"></div>
    </div>

    <script>
        function getGrades() {
            const nationalCode = document.getElementById('nationalCode').value.trim();
            const resultElement = document.getElementById('result');
            
            if (!nationalCode) {
                showError("لطفا کد ملی را وارد کنید");
                return;
            }
            
            if (nationalCode.length !== 10 || !/^\d+$/.test(nationalCode)) {
                showError("کد ملی باید ۱۰ رقم باشد");
                return;
            }
            
            // در واقعیت از این خط استفاده کن:
            // fetch('https://raw.githubusercontent.com/username/repo/main/grades.json')
            //     .then(response => response.json())
            //     .then(studentsData => {
            
            const studentsData = {
                "students": [
                    {
                        "student_id": "1",
                        "first_name": "علي",
                        "last_name": "رضاعي", 
                        "national_code": "0012345678",
                        "class": "901",
                        "art": "18",
                        "sport": "19", 
                        "language": "17",
                        "technology": "16",
                        "social_studies": "18",
                        "writing": "19",
                        "spelling": "17",
                        "persian_literature": "18",
                        "math": "19",
                        "science": "17",
                        "arabic": "16",
                        "thinking": "18",
                        "religion": "19",
                        "quran": "17",
                        "positive": "18.5",
                        "defense": "19"
                    }
                ]
            };
            
            const student = studentsData.students.find(s => s.national_code === nationalCode);
            
            if (student) {
                showAllGrades(student);
            } else {
                showError("❌ دانش آموزی با این کد ملی یافت نشد");
            }
            
            // }) // این خط برای fetch واقعی
            // .catch(error => {
            //     showError("⚠️ خطا در ارتباط با سرور");
            // });
        }
        
        function showAllGrades(student) {
            const hasDefense = student.defense !== undefined;
            
            let defenseRow = '';
            if (hasDefense) {
                defenseRow = `<tr><td>آمادگی دفاعی</td><td>${student.defense}</td></tr>`;
            }
            
            document.getElementById('result').innerHTML = `
                <div class="grade-card">
                    <h3 style="color: #2e7d32; margin-bottom: 15px;">📋 نمرات تحصیلی</h3>
                    
                    <div class="student-info">
                        <p style="font-size: 18px; margin: 10px 0; font-weight: bold;">
                            ${student.first_name} ${student.last_name}
                        </p>
                        <p style="font-size: 14px; margin: 5px 0; color: #666;">
                            <span class="class-badge">کلاس ${student.class}</span>
                            <strong>کد ملی:</strong> ${student.national_code}
                        </p>
                    </div>
                    
                    <table>
                        <tr>
                            <th>درس</th>
                            <th>نمره</th>
                        </tr>
                        <tr><td>هنر</td><td>${student.art}</td></tr>
                        <tr><td>ورزش</td><td>${student.sport}</td></tr>
                        <tr><td>زبان خارجی</td><td>${student.language}</td></tr>
                        <tr><td>کار و فناوری</td><td>${student.technology}</td></tr>
                        <tr><td>مطالعات اجتماعی</td><td>${student.social_studies}</td></tr>
                        <tr><td>نگارش</td><td>${student.writing}</td></tr>
                        <tr><td>املا</td><td>${student.spelling}</td></tr>
                        <tr><td>ادبیات فارسی</td><td>${student.persian_literature}</td></tr>
                        <tr><td>ریاضی</td><td>${student.math}</td></tr>
                        <tr><td>علوم تجربی</td><td>${student.science}</td></tr>
                        <tr><td>عربی</td><td>${student.arabic}</td></tr>
                        <tr><td>تفکر و سبک زندگی</td><td>${student.thinking}</td></tr>
                        <tr><td>دینی</td><td>${student.religion}</td></tr>
                        <tr><td>قرآن</td><td>${student.quran}</td></tr>
                        <tr><td>مثبت یک</td><td>${student.positive}</td></tr>
                        ${defenseRow}
                    </table>
                    
                    <div style="margin-top: 15px; font-size: 12px; color: #666;">
                        <p>📅 تاریخ: ${new Date().toLocaleDateString('fa-IR')}</p>
                    </div>
                </div>
            `;
        }
        
        function showError(message) {
            document.getElementById('result').innerHTML = `
                <div class="error-message">
                    <p style="margin: 0;">${message}</p>
                </div>
            `;
        }
        
        // اجازه دادن به Enter برای جستجو
        document.getElementById('nationalCode').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                getGrades();
            }
        });
    </script>
</body>
</html>