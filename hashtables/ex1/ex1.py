def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    if len(weights) < 2:
        return None

    index = 0

    for weight in weights:
        if limit - weight in cache:
            return(index, cache[limit - weight])
        cache[weight] = index
        index += 1

    return None
