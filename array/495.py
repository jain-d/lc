# Teemo Attacking

def find_poisoned_duration(time_series: list[int], duration: int) -> int:
    poisoned_till: range
    previously_poisoned_duration = 0
    if duration:
        for index, value in enumerate(time_series):
            if index == 0:
                poisoned_till = range(value, value + duration)
                continue
            if value in poisoned_till:
                previously_poisoned_duration += (value - poisoned_till.start)
            else:
                previously_poisoned_duration += poisoned_till.stop - poisoned_till.start
            poisoned_till = range(value, value + duration)
        total_poisoned_duration = previously_poisoned_duration + poisoned_till.stop - poisoned_till.start
        return total_poisoned_duration
                

    return duration




inputs: tuple = (([1, 4], 2), ([1, 2], 2), ([1, 3], 0), ([0], 1), ([1, 1], 1))

for i in inputs:
    print(i, "\t\t", find_poisoned_duration(*i))
