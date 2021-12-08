from knapsack.Knapsack import Knapsack


def solve_knapsack_greedy(knapsack, objects_dict) -> Knapsack:
    assert(knapsack.content == [])
    filled_sack = knapsack

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
    pass

