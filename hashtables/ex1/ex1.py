def get_indices_of_item_weights(weights, length, limit):
    """
    what's length got to do, got to do with this? who needs a length, when a length is not needed
    what's length, but a second func paramiter
    -- famous words by Tina Turner... python hacker extraorinaire 
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
