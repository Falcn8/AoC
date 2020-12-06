import pyperclip # to copy
f = open("day2-input.txt", "r") # ==
success = 0
for line in f:
    s = [] # ==
    s = line.strip().split(": ") # s = ["1-3 a", "abcde"]
    tb = s[1] # tb = "abcde"
    ta = [] # ==
    ta = s[0].split() # ta = ["1-3", "a"]
    l = ta[1] # l = "a"
    r = ta[0].split("-") # r = ["1", "3"]
    first = int(r[0]) # r[0] = 1
    last = int(r[1]) # r[1] = 3
    occur = 0
    times = 0
    for i in tb:
        times += 1
        if times == first or times == last:
            if i == l:
                occur += 1
    if occur == 1:
        success += 1
print(success)
pyperclip.copy(success) # the answer copies to your clipbored