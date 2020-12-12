import pyperclip
import sys

f = open("day4-input.txt", "r")
valid = 0
curr_l = 1
data = ""
total_pass = 284
passe = 0
total_l = 1056

while True:
    for line in f:
        if curr_l != total_l:
            line = line.strip()
            if line == "":
                if "byr:" in data and "iyr:" in data and "eyr:" in data and "hgt:" in data and "hcl:" in data and "ecl:" in data and "pid:" in data:
                    valid += 1
                data = ""
            else: 
                data += line
            curr_l += 1
        else:
            print(valid)
            pyperclip.copy(valid)
            sys.exit(0)