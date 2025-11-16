<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سامانه نمرات تحصیلی</title>
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
        }
        
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 30px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
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
        }
        
        button:hover {
            background: #45a049;
        }
        
        .grade-card {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            margin: 25px 0;
            border: 2px solid #e9ecef;
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
        
        .error-message {
            background: #ffebee;
            color: #c62828;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎓 سامانه نمرات تحصیلی</h1>
    </div>

    <div class="container">
        <h2>مشاهده نمرات با کد ملی</h2>
        
        <input type="text" id="nationalCode" placeholder="کد ملی خود را وارد کنید">
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

            // در واقعیت از این خط استفاده کن:
            fetch('https://raw.githubusercontent.com/username/repo/main/grades.json')
                .then(response => response.json())
                .then(studentsData => {
                    const student = studentsData.students.find(s => s.national_code === nationalCode);
                    
                    if (student) {
                        showAllGrades(student);
                    } else {
                        showError("❌ دانش آموزی با این کد ملی یافت نشد");
                    }
                })
                .catch(error => {
                    showError("⚠️ خطا در ارتباط با سرور");
                });
        }
        
        function showAllGrades(student) {
            const hasDefensive = student.defensive !== undefined;
            
            let defensiveRow = '';
            if (hasDefensive) {
                defensiveRow = `<tr><td>دفاعی</td><td>${student.defensive}</td></tr>`;
            }
            
            document.getElementById('result').innerHTML = `
                <div class="grade-card">
                    <h3>📋 نمرات تحصیلی</h3>
                    <p><strong>${student.first_name} ${student.last_name}</strong></p>
                    <p>کد ملی: ${student.national_code}</p>
                    
                    <table>
                        <tr>
                            <th>درس</th>
                            <th>نمره</th>
                        </tr>
                        <tr><td>هنر</td><td>${student.art}</td></tr>
                        <tr><td>ورزش</td><td>${student.sport}</td></tr>
                        <tr><td>انگلیسی</td><td>${student.english}</td></tr>
                        <tr><td>فناوری</td><td>${student.technology}</td></tr>
                        <tr><td>مطالعات اجتماعی</td><td>${student.social_studies}</td></tr>
                        <tr><td>نگارش</td><td>${student.writing}</td></tr>
                        <tr><td>املا</td><td>${student.dictation}</td></tr>
                        <tr><td>ادبیات</td><td>${student.literature}</td></tr>
                        <tr><td>ریاضی</td><td>${student.math}</td></tr>
                        <tr><td>علوم</td><td>${student.science}</td></tr>
                        <tr><td>عربی</td><td>${student.arabic}</td></tr>
                        <tr><td>تفکر و سبک زندگی</td><td>${student.thinking_lifestyle}</td></tr>
                        <tr><td>دینی</td><td>${student.religious}</td></tr>
                        <tr><td>قرآن</td><td>${student.quran}</td></tr>
                        ${defensiveRow}
                        <tr><td>مثبت یک</td><td>${student.plusone}</td></tr>
                    </table>
                </div>
            `;
        }
        
        function showError(message) {
            document.getElementById('result').innerHTML = `
                <div class="error-message">
                    <p>${message}</p>
                </div>
            `;
        }
        
        document.getElementById('nationalCode').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                getGrades();
            }
        });
    </script>
</body>
</html>