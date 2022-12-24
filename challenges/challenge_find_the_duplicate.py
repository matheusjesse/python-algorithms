def find_duplicate(nums):
    if nums:
        sort_list = sorted(nums)

        new_list = []

        for num in sort_list:
            if type(num) is not int or num < 0:
                return False
            if num not in new_list:
                new_list.append(num)
            else:
                return num

    return False
