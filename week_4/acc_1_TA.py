def perm(nums):
    # print("This function is running!")
    # print(nums)
    

    if len(nums) == 1:
        # print("One round stopped!")
        return [nums]

    result = []

    for i in range(len(nums)):
       m = nums[i]
    #    print("------------------------")
    #    print("Value of m:",m)

       rest = nums[:i] + nums[i+1:]
       
       for p in perm(rest):
           result.append([m] + p) 

    return result
 


def main():

    num = input().split()
    result = perm(num)
    for i in result: print(i)

main()