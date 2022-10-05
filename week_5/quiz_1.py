def intersection(lsts):

    elements = []
    for elem in lsts[0]:
        condition = elem not in elements
        for lst in lsts[1:]:
            if elem not in lst:
                condition = False
        if condition:
            elements = elements + [elem]
    return elements

def main():

    lsts = []
    num = int(input())
    for _ in range(num):
        tempList = input().split()
        lsts.append(tempList)
    print(intersection(lsts))

main()