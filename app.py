from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# وظيفة للبحث في قاعدة البيانات
def get_patient(p_id):
    conn = sqlite3.connect('shield_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id_number=?", (p_id,))
    patient = cursor.fetchone()
    conn.close()
    return patient

# 1. الصفحة الرئيسية (Identification)
@app.route('/')
def index():
    return render_template('login.html')

# 2. صفحة البيانات الكبرى (Dashboard)
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    p_id = request.form.get('patient_id')
    patient_data = get_patient(p_id)
    if patient_data:
        return render_template('dashboard.html', p=patient_data)
    else:
        return render_template('login.html', error="ID not found in  system")
if __name__ == '__main__':
    # تشغيل السيرفر على البورت 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
