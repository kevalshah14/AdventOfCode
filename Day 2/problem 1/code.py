mainList = []

sum = 0
with open('Day 2/problem 1/input.txt', 'r') as file:
    for line in file:
        tempList = []
        for num in line.strip().split():
            tempList.append(int(num))
        mainList.append(tempList)
def isdecreasing(lst):
    for i in range(0,len(lst)-1):
        if lst[i] > lst[i+1] and lst[i] - lst[i+1] < 4 and lst[i] - lst[i+1] > 0:
            continue
        else:
            return False
    return True
def isincreasing(lst):
    for i in range(0,len(lst)-1):
        if lst[i] < lst[i+1] and lst[i+1] - lst[i] < 4 and lst[i+1] - lst[i] > 0:
            continue
        else:
            return False
    return True

for i in mainList:
    if isdecreasing(i):
        sum +=1
    elif isincreasing(i):
        sum +=1
    else:
        continue
print(sum)
        