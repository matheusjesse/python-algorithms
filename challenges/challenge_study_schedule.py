def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None

    students_count = 0

    for entry, exit in permanence_period:
        if type(entry) is not int or type(exit) is not int:
            return None

        if entry <= target_time <= exit:
            students_count += 1
    
    return students_count