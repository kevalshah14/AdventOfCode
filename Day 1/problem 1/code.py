list1, list2 = [], []
sum = 0
with open('Day 1/problem 1/input.txt', 'r') as file:
    for line in file:
        col1, col2 = line.strip().split() 
        list1.append(int(col1))  
        list2.append(int(col2))



for i in range(len(list1)):
    diff = max(min(list1),min(list2)) - min(min(list1),min(list2))
    list1.remove(min(list1))
    list2.remove(min(list2))
    sum += diff
print(sum)
    