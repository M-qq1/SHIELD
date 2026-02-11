from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# بيانات المريض الافتراضية لعرضها في الداشبورد
PATIENT_DATA = {
    "1098765432": {
        "name": "Abdulaziz Al-Saad",
        "age": 45,
        "gender": "Male",
        "blood": "+A",
        "condition": "Critical",
        "notes": "Asthma, GERD",
        "protocol": "Salbutamol Nebulizer, Monitor SpO2"
    }
}

# 1. صفحة التحقق (الرئيسية - اللي فيها البصمة والوجه)
@app.route('/')
def index():
    return render_template('index.html')

# 2. صفحة المعلومات (الداشبورد المطور)
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # نأخذ رقم الهوية من البحث أو نضع الرقم الافتراضي للعرض
    patient_id = request.form.get('patient_id', '1098765432')
    data = PATIENT_DATA.get(patient_id)
    
    # الحصول على الوقت الحالي للعرض في الهيدر
    current_time = datetime.now().strftime("%H:%M")
    
    return render_template('dashboard.html', patient=data, time=current_time)

if name == '__main__':
    app.run(debug=True)
