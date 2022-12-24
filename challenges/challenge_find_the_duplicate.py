def find_duplicate(nums):
    if not nums or len(nums) <= 1 or type(nums) is not list:
        return False

    newlist = []
    dupli = []

    for num in nums:
        if num not in newlist:
            newlist.append(num)
        else:
            return num

    return False
