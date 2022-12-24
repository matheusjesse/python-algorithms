def find_duplicate(nums):
    if nums or len(nums) > 1:
        sort_list = sorted(nums)

        for index in range(len(sort_list) - 1):
            if type(sort_list[index]) is not int or sort_list[index] < 0:
                return False
            if sort_list[index] == sort_list[index + 1]:
                return sort_list[index]

    return False
