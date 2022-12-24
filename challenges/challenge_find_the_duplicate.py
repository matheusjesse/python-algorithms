def find_duplicate(nums):
    if not nums or len(nums) <= 1 or type(nums) is not list:
        return False

    sort_list = nums.sort()

    newlist = []
    dupli = []
    for num in sort_list:
        if num not in newlist:
            newlist.append(num)
        else:
            dupli.append(num)

        if len(dupli) > 0:
            return dupli[0]

    return False
