import re

pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"

mul_enabled = True
results = []
ans = 0
with open("Day 3/problem 2/input.txt", "r") as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "do()":
                mul_enabled = True
            elif match == "don't()":
                mul_enabled = False
            elif mul_enabled and match.startswith("mul"):
                if re.match(r"mul\(\d+,\d+\)", match):  
                    x, y = map(int, re.findall(r"\d+", match))
                    results.append((x, y))

for x, y in results:
    ans += int(x) * int(y)
print(ans)
