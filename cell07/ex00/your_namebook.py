#!/usr/bin/env python3

def array_of_names(persons):
    # สร้าง list ว่างสำหรับเก็บชื่อเต็ม
    full_names = []

    # loop ผ่าน key (first name) และ value (last name) ใน dictionary
    for first, last in persons.items():
        # ทำให้ขึ้นต้นด้วยตัวใหญ่ทั้ง first และ last
        first_cap = first.capitalize()
        last_cap = last.capitalize()
        
        # รวมเป็นชื่อเต็ม
        full_name = first_cap + " " + last_cap
        
        # เก็บลงใน list
        full_names.append(full_name)

    return full_names


# ทดสอบการทำงาน
if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }

    print(array_of_names(persons))
