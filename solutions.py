from knapsack.Knapsack import Knapsack


def solve_knapsack_greedy(knapsack, objects_dict) -> Knapsack:
    assert(knapsack.content == [])
    filled_sack = knapsack.copy()

    sorted_objects_dict = dict(sorted(objects_dict.items(), key=lambda x: x[1][0]/x[1][1], reverse=True))
    weight = 0

    for item in sorted_objects_dict.items():
        if weight + item[1][1] <= filled_sack.capacity:
            filled_sack.content.append(item[0])
            weight += item[1][1]

    return filled_sack


def solve_knapsack_best(knapsack, objects_dict) -> Knapsack:
    pass


def solve_knapsack_optimal(knapsack, objects_dict) -> Knapsack:
    knapsack_optimal = knapsack.copy()
    objects_dict_iterated = objects_dict.copy()
    objects_dict_iterated = list(objects_dict_iterated.items())

    return solve_knapsack_optimal_recursive(knapsack_optimal, objects_dict, objects_dict_iterated, 0)


def solve_knapsack_optimal_recursive(knapsack, objects_dict, objects_list, i) -> Knapsack:
    if i >= len(objects_list):
        return knapsack

    sack_left = knapsack.copy()
    sack_right = knapsack.copy()

    if knapsack.get_value_and_weight(objects_dict)[1] + objects_list[i][1][1] <= knapsack.capacity:
        sack_left.content.append(objects_list[i][0])
        sack_left = solve_knapsack_optimal_recursive(sack_left, objects_dict, objects_list, i + 1)

    sack_right = solve_knapsack_optimal_recursive(sack_right, objects_dict, objects_list, i + 1)

    if sack_left.get_value_and_weight(objects_dict)[0] > sack_right.get_value_and_weight(objects_dict)[0]:
        return sack_left
    return sack_right
