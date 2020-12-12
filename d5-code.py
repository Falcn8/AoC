import pyperclip
seats = [(int("".join(map(lambda x: "1" if x in "BR" else "0", s.rstrip())), 2)) for s in open("day5-input.txt")]
print(f"Highest: {max(seats)}\tYour seat: {next(filter(lambda x: x not in seats, range(min(seats), max(seats))))}")
highest = max(seats)
pyperclip.copy(highest)