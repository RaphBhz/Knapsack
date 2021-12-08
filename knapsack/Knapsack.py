class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []

    def get_value_and_weight(self, objects_dict) -> (int, int):
        value = 0
        weight = 0

        for s in self.content:
            value += objects_dict.get(s)[0]
            weight += objects_dict.get(s)[1]

        return value, weight

    def print_content(self, objects_dict) -> None:
        count = 0

        for s in self.content:
            print(s + " " + str(objects_dict.get(s)[0]) + " " + str(objects_dict.get(s)[1]))
            count += 1

        print("Le sac a " + str(count) + " objets, pour une valeur de " +
              str(self.get_value_and_weight(objects_dict)[0]) + " et un poids de " +
              str(self.get_value_and_weight(objects_dict)[1]) + "/" + str(self.capacity))

        return
