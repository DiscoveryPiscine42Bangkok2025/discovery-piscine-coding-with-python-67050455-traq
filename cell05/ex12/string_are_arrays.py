import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    found = False
    
    for ch in text:
        if ch == "z" or ch == "Z":
            print("z")
            found = True
    
    if not found:
        print("none")
