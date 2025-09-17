import sys

def shrink(text):
    print(text[:8])  # ใช้ slice เอา 8 ตัวแรก

def enlarge(text):
    while len(text) < 8:
        text += "Z"
    print(text)

args = sys.argv[1:]

if len(args) < 1:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
