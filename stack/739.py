# Daily Temperature

def daily_temperature(temperatures: list[int]) -> list[int]:
    warmer_days: list[int] = [0] * len(temperatures)
    temperature_stack: list[int] = []

    for index in range(len(temperatures)):
        while temperature_stack and temperatures[index] > temperatures[temperature_stack[-1]]:
            day = temperature_stack.pop()
            warmer_days[day] = index - day

        temperature_stack.append(index)

    return warmer_days


inputs = (([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]), ([30,40,50,60], [1,1,1,0]), ([30, 60, 90], [1, 1, 0]))

for input in inputs:
    if input[1] == (result := daily_temperature(input[0])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nfor {input}, {result}")
