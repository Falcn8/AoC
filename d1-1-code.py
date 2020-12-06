import pyperclip 
f_in = open("day1-input.txt", "r")
v = []
for s in f_in:
    v.append(int(s.strip("\n")))
f_in.close()
for a in v:
    for b in v:
        if a + b == 2020:
            print(a*b)
            pyperclip.copy(str(a*b))
            break
