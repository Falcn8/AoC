import pyperclip # to copy
f = open("day2-input.txt", "r") # ==
success = 0 # ==
for line in f: # line = "1-3 a: abcde"
    s = [] # ==
    s = line.strip().split(": ") # s = ["1-3 a", "abcde"]
    tb = s[1] # tb = "abcde"
    ta = [] # ==
    ta = s[0].split() # ta = ["1-3", "a"]
    l = ta[1] # l = "a"
    r = ta[0].split("-") # r = ["1", "3"]
    r[0] = int(r[0]) # r[0] = 1
    r[1] = int(r[1]) # r[1] = 3
    times_l = 0 # ==
    for i in tb: # repeat through the string (tb)
        if i == l: # check to see if the character is (l)
            times_l += 1 # ==
    if times_l in range(r[0], r[1]+1): # if the times (l) appeared is in the range...
        success += 1 # add success times by 1
print(success) # ==
pyperclip.copy(success) # the answer copies to your clipbored 