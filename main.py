import time

def mostFactors(min, max, step = 1):
    current_highest = 1
    most_factors = []
    for x in range(min, max + 1, step):
        factor_counter = 0
        for y in range(1, x + 1):
            if x % y == 0:
                factor_counter += 1
        digit_counter = 0
        x2 = x
        while x2 != 0:
            x2 = x2 // 10
            digit_counter += 1
        ratio = factor_counter / digit_counter
        if ratio > current_highest:
            current_highest = ratio
            most_factors = [(x, ratio)]
        elif ratio == current_highest:
            most_factors.append((x, ratio))
    return most_factors

startTime = time.time_ns()
print("START TIME: " + str(startTime))

print(mostFactors(1, 1000000, 1))

endTime = time.time_ns
print("END TIME: " + str(endTime))

print("TOTAL TIME: " + str(endTime - startTime))