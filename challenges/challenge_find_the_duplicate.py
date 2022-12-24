def find_duplicate(nums):
    if nums:
        sort_list = nums.sort()

        newlist = []
        dupli = []
        for num in sort_list:
            if num not in newlist:
                newlist.append(num)
            if num not in dupli:
                dupli.append(num)

            if len(dupli) > 0:
                return dupli[0]

    return False
