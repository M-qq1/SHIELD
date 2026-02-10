import sqlite3

connection = sqlite3.connect('shield_database.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS patients")

# إنشاء الجدول بترتيب دقيق يمنع اللخبطة
cursor.execute('''
    CREATE TABLE patients (
        id_number TEXT PRIMARY KEY,
        full_name TEXT,
        age INTEGER,
        gender TEXT,
        blood_type TEXT,
        insurance TEXT,
        chronic_conditions TEXT,
        allergies TEXT,
        current_meds TEXT,
        contraindications TEXT,
        suggested_protocol TEXT
    )
''')

# حالات طبية مختلفة (Cardiac, Asthma, Diabetic Emergency)
patients_list = [
    # حالة قلب (Chest Pain)
    ('1033331223', 'Abdulaziz A', 37, 'Male', 'O+', 'Active', 'Hypertension', 'Aspirin', 'Lisinopril', 'NO Aspirin (Allergic)', 'ACS Protocol: ECG, Oxygen, Nitro (if BP stable)'),
    
    # حالة تنفسية (Asthma)
    ('1098765432', 'Abdulaziz Al-Saad', 45, 'Male', 'A+', 'Active', 'Asthma, GERD', 'None', 'Ventolin', 'None', 'Respiratory Protocol: Salbutamol Nebulizer, Monitor SpO2'),
    
    # حالة سكر (Hypoglycemia)
    ('2011223344', 'Omar Al-Farouk', 50, 'Male', 'B-', 'Expired', 'Type 1 Diabetes', 'Sulfa', 'Insulin', 'None', 'Diabetic Protocol: Check Glucometer, Administer D50 if <60mg/dL')
]

cursor.executemany("INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?,?,?)", patients_list)
connection.commit()
connection.close()
print("تم تحديث الداتا بيس بحالات طبية واقعية!")