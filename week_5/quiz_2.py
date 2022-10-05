def isPerfect(num):

    numList = []
    index = 1
    while index < num:
        if(num % index == 0):
            numList.append(index)
        index += 1

    totalsum = 0
    for i in range(len(numList)):
        totalsum = totalsum + numList[i-1]

    if(totalsum == num):
        return True
    else:
        return False

minNum, maxNum = input("m n: ").split(" ")

minNum = int(minNum)
maxNum = int(maxNum)

list1 = []
i = minNum
while i <= maxNum:
    if(isPerfect(i)):
        list1.append(i)
    i += 1

for j in range(len(list1)):
    if j < len(list1)-1:
        print(list1[j], end=" ")
    else:
        print(list1[j])


