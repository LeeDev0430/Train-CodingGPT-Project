def dice_sum_possibilities(dice_count, desired_sum):
    # table to store solutions to subproblems
    # table[i][j] will represent number of ways i dice can produce sum j
    table = [[0] * (desired_sum + 1) for _ in range(dice_count + 1)]

    # one way to produce sum 0 with 0 dice
    table[0][0] = 1

    # fill the table in bottom-up manner
    for i in range(1, dice_count + 1):
        for j in range(1, desired_sum + 1):
            for face in range(1, 7):
                if j >= face:
                    table[i][j] += table[i - 1][j - face]

    return table[dice_count][desired_sum]

dice_count = 6
desired_sum = 18

possible_combinations = dice_sum_possibilities(dice_count, desired_sum)
total_outcomes = 6**6
probability = possible_combinations / total_outcomes

print(probability)