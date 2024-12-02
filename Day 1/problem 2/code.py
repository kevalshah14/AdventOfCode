list1, list2 = [], []
score = 0
with open('Day 1/problem 1/input.txt', 'r') as file:
    for line in file:
        col1, col2 = line.strip().split() 
        list1.append(int(col1))  
        list2.append(int(col2))

for i in range(len(list1)):
    list2.count(list1[i])
    tempscore = list2.count(list1[i]) * list1[i]
    score += tempscore
print(score)
    