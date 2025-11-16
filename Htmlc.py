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
        
        .input-group {
            margin: 20px 0;
        }
        
        input {
            width: 100%;
            max-width: 400px;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
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
            transition: all 0.3s ease;
        }
        
        button:hover {
            background: #45a049;
            transform: translateY(-2px);
        }
        
        .loading {
            display: none;
            color: #667eea;
            margin: 20px 0;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .grade-card {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            margin: 25px 0;
            border: 2px solid #e9ecef;
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
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
            font-weight: bold;
        }
        
        tr:nth-child(even) {
            background: #f8f9fa;
        }
        
        tr:hover {
            background: #e3f2fd;
        }
        
        .error-message {
            background: #ffebee;
            color: #c62828;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-right: 4px solid #c62828;
        }
        
        .success-message {
            background: #e8f5e8;
            color: #2e7d32;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-right: 4px solid #2e7d32;
        }
        
        @media (max-width: 768px) {
            .container {
                margin: 10px;
                padding: 20px;
            }
            
            table {
                font-size: 12px;
            }
            
            th, td {
                padding: 8px 4px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎓 سامانه نمرات تحصیلی</h1>
        <p>مدرسه نمونه - سال تحصیلی ۱۴۰۳</p>
    </div>

    <div class="container">
        <h2>مشاهده نمرات با کد ملی</h2>
        
        <div class="input-group">
            <input type="text" id="nationalCode" placeholder="کد ملی خود را وارد کنید" maxlength="10">
        </div>
        
        <button onclick="getGrades()">🔍 مشاهده نمرات</button>
        
        <div class="loading" id="loading">
            <div class="spinner"></div>
            در حال دریافت اطلاعات...
        </div>
        
        <div id="result"></div>
    </div>

    <script>
        // 🔄 این لینک رو با لینک واقعی فایل JSON در گوگل درایو عوض کن
        const JSON_URL = 'https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_HERE';
        
        function getGrades() {
            const nationalCode = document.getElementById('nationalCode').value.trim();
            const loadingElement = document.getElementById('loading');
            const resultElement = document.getElementById('result');
            
            // اعتبارسنجی
            if (!nationalCode) {
                showError("لطفا کد ملی را وارد کنید");
                return;
            }
            
            if (nationalCode.length !== 10 || !/^\d+$/.test(nationalCode)) {
                showError("کد ملی باید ۱۰ رقم باشد");
                return;
            }
            
            // نمایش loading
            loadingElement.style.display = 'block';
            resultElement.innerHTML = '';
            
            // دریافت داده از گوگل درایو
            fetch(JSON_URL)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('خطا در دریافت اطلاعات');
                    }
                    return response.json();
                })
                .then(studentsData => {
                    loadingElement.style.display = 'none';
                    
                    const student = studentsData.students.find(s => s.national_code === nationalCode);
                    
                    if (student) {
                        showAllGrades(student);
                    } else {
                        showError("❌ دانش آموزی با این کد ملی یافت نشد");
                    }
                })
                .catch(error => {
                    loadingElement.style.display = 'none';
                    showError("⚠️ خطا در ارتباط با سرور. لطفا دوباره تلاش کنید.");
                    console.error('Error:', error);
                });
        }
        
        function showAllGrades(student) {
            const hasDefensive = student.defensive !== undefined;
            
            let defensiveRow = '';
            if (hasDefensive) {
                defensiveRow = `<tr><td>آمادگی دفاعی</td><td>${student.defensive}</td></tr>`;
            }
            
            document.getElementById('result').innerHTML = `
                <div class="grade-card">
                    <h3 style="color: #2e7d32; margin-bottom: 15px;">✅ کارنامه تحصیلی</h3>
                    
                    <div class="student-info">
                        <p style="font-size: 18px; margin: 10px 0; font-weight: bold;">
                            ${student.first_name} ${student.last_name}
                        </p>
                        <p style="font-size: 14px; margin: 5px 0; color: #666;">
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
                    
                    <div style="margin-top: 15px; font-size: 12px; color: #666;">
                        <p>📅 تاریخ استعلام: ${new Date().toLocaleDateString('fa-IR')}</p>
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
        
        function showSuccess(message) {
            document.getElementById('result').innerHTML = `
                <div class="success-message">
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
        
        // فوکوس خودکار روی input
        document.getElementById('nationalCode').focus();
    </script>
</body>
</html>