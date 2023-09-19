def max_duffel_bag_value(cake_tuples, capacity):
    max_values = [0] * (capacity + 1)

    for current_capacity in range(capacity + 1):
        for cake_weight, cake_value in cake_tuples:
            if cake_weight <= current_capacity:
                max_value = cake_value + max_values[current_capacity - cake_weight]
                max_values[current_capacity] = max(max_values[current_capacity], max_value)

    return max_values[capacity]
