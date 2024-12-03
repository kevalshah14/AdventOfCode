import re

pattern = r"mul\((\d+),(\d+)\)"
ans = 0
with open("Day 3/problem 1/input.txt", "r") as file:
    input_text = file.read()

matches = re.findall(pattern, input_text)

for x, y in matches:
    temp = int(x) * int(y)
    ans += temp
print(ans)
