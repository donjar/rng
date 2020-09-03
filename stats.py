from random import random

def calculate_bot_input(user_input):
    memory = {}
    res = []

    for i in range(len(user_input)):
        prob = 0.5
        curr_code = ""
        for j in range(1, 5):
            if (i - j < 0):
                break

            curr = user_input[i - j]
            curr_code += ("T" if curr else "F")
            if memory.get(curr_code) is None:
                break
            prob += 1 * (1 if j == 4 else 0) * (0.5 - memory[curr_code][0] / memory[curr_code][1])

        res.append(random() >= prob)

        code = ""
        for j in range(1, 5):
            if (i - j < 0):
                break

            curr = user_input[i - j]
            code += ("T" if curr else "F")
            if memory.get(code) is None:
                memory[code] = [0, 0]

            memory[code][0] += (1 if curr else 0)
            memory[code][1] += 1

    return res

x = [0 for _ in range(51)]
for i in range(100000):
    if i % 10000 == 0:
        print(i)

    user_input = [random() > 0.5 for __ in range(50)]
    bot_input = calculate_bot_input(user_input)
    m = sum(a == b for a, b in zip(bot_input, user_input))
    x[m] += 1
