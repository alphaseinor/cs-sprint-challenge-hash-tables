def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for number in a:
        if number not in cache and number != 0: #serously... 0? come on! it's positive, it's negative, it's an empty value, just like my heart... what an edge case!!!
            cache[number] = number
            if -number in cache: #didn't know -number could exist until this day... very cool!
                result.append(abs(number)) #well... needs to be positive, so abs get a good workout

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
