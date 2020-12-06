import pyperclip 
f_in = open("day1-input.txt", "r")
v = []
for s in f_in:
    v.append(int(s.strip("\n")))
f_in.close()
for a in v:
    for b in v:
        for c in v:
            if a + b + c == 2020:
                print(a*b*c)
                pyperclip.copy(str(a*b*c))
                break
