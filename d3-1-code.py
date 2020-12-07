import pyperclip # to copy
f = open("day3-input.txt", "r") # ==
#### 31 Blocks | 323 Lines ###
input_file = f.readlines()
input_file = [line.replace('\n','') for line in input_file]
right_counter = 3
count_trees = 0
for index, line in enumerate(input_file):
    if index > 0:
        if list(line)[right_counter] == '#':
            count_trees+=1
        right_counter+=3
        if right_counter >= len(line):
            right_counter = right_counter-len(line)
print(count_trees)
pyperclip.copy(count_trees) # the answer copies to your clipbored 