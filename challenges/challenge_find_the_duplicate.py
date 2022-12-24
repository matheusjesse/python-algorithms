def find_duplicate(nums):
    if nums:
        sort_list = sorted(nums)

        newlist = []

        for num in sort_list:
            if num not in newlist:
                newlist.append(num)
            else:
                return num

    return False
