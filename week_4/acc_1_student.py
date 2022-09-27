#########################
# Written by Man Kwun Po
#########################

def main():

    nums = input().split()
  
    if len(nums)==3:
        for i in nums:
            for ii in nums:
                for iii in nums:
                    if i!=ii and i!=iii and ii!=iii:
                        print(f"['{i}', '{ii}', '{iii}']")
    if len(nums)==4:                    
        for i in nums:
            for ii in nums:
                for iii in nums:
                    for iiii in nums:
                        if i!=ii and i!=iii and ii!=iii and iiii!=i and ii!=iiii and iii!=iiii:
                            print(f"['{i}', '{ii}', '{iii}', '{iiii}']")
    if len(nums)==5:
        for i in nums:
            for ii in nums:
                for iii in nums:
                    for iiii in nums:
                        for iiiii in nums:
                            if i!=ii and i!=iii and ii!=iii and iiii!=i and ii!=iiii and iii!=iiii and i!=iiiii and ii!=iiiii and iii!=iiiii and iiii!=iiiii:
                                print(f"['{i}', '{ii}', '{iii}', '{iiii}', '{iiiii}']")

    if len(nums)==6:
        for i in nums:
            for ii in nums:
                for iii in nums:
                    for iiii in nums:
                        for iiiii in nums:
                            for iiiiii in nums:
                                if i!=ii and i!=iii and ii!=iii and iiii!=i and ii!=iiii and iii!=iiii and i!=iiiii and ii!=iiiii and iii!=iiiii and iiii!=iiiii and i!=iiiiii and ii!=iiiiii and iii!=iiiiii and iiii!=iiiiii and iiiii!=iiiiii:
                                    print(f"['{i}', '{ii}', '{iii}', '{iiii}', '{iiiii}','{iiiiii}']")
    if len(nums)==7:
        for i in nums:
            for ii in nums:
                for iii in nums:
                    for iiii in nums:
                        for iiiii in nums:
                            for iiiiii in nums:
                                for iiiiiii in nums:
                                    if i!=ii and i!=iii and ii!=iii and iiii!=i and ii!=iiii and iii!=iiii and i!=iiiii and ii!=iiiii and iii!=iiiii and iiii!=iiiii and i!=iiiiii and ii!=iiiiii and iii!=iiiiii and iiii!=iiiiii and iiiii!=iiiiii and i!=iiiiiii and ii!=iiiiiii and iii!=iiiiiii and iiii!=iiiiiii  and iiiii!=iiiiiii and iiiiii!=iiiiiii:
                                        print(f"['{i}', '{ii}', '{iii}', '{iiii}', '{iiiii}','{iiiiii}'],'{iiiiiii}'")

    if len(nums)==8:
        for i in nums:
            for ii in nums:
                for iii in nums:
                    for iiii in nums:
                        for iiiii in nums:
                            for iiiiii in nums:
                                for iiiiiii in nums:
                                    for iiiiiiii in nums:
                                        if i!=ii!=iii!=iiii!=iiiii!=iiiiii!=iiiiiii:
                                            print(f"['{i}', '{ii}', '{iii}', '{iiii}', '{iiiii}','{iiiiii}'],'{iiiiiii}','{iiiiiiii}'")
    if len(nums)==9:
        for i in nums:
            for ii in nums:
                for iii in nums:
                    for iiii in nums:
                        for iiiii in nums:
                            for iiiiii in nums:
                                for iiiiiii in nums:
                                    for iiiiiiiii in nums:
                                        if i!=ii!=iii!=iiii!=iiiii!=iiiiii!=iiiiiii:
                                            print(f"['{i}', '{ii}', '{iii}', '{iiii}', '{iiiii}','{iiiiii}'],'{iiiiiii}','{iiiiiiii}','{iiiiiiiii}'")
    if len(nums)==10:
        for i in nums:
            for ii in nums:
                for iii in nums:
                    for iiii in nums:
                        for iiiii in nums:
                            for iiiiii in nums:
                                for iiiiiii in nums:
                                    for iiiiiiiii in nums:
                                        for iiiiiiiiii in nums:
                                            if i!=ii!=iii!=iiii!=iiiii!=iiiiii!=iiiiiii!=iiiiiiiiii:
                                                print(f"['{i}', '{ii}', '{iii}', '{iiii}', '{iiiii}','{iiiiii}'],'{iiiiiii}','{iiiiiiii}','{iiiiiiiii}','{iiiiiiiiii}'")

main()