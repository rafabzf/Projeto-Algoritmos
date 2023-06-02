def study_schedule(permanence_period, target_time):
    if not permanence_period or not target_time:
        return None

    count = 0
    for period in permanence_period:
        if (
            type(period) != tuple
            or len(period) != 2
            or type(period[0]) != int
            or type(period[1]) != int
            or period[0] > period[1]
            or period[0] < 0
            or period[1] < 0
        ):
            return None

        if period[0] <= target_time <= period[1]:
            count = count + 1

    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_period, 1))
