# เก็บรหัสไว้ในตัวแปร
password = "67050455"

# ให้ผู้ใช้กรอกรหัส
user_input = input("Enter password: ")

# ตรวจสอบว่าตรงกันหรือไม่
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
