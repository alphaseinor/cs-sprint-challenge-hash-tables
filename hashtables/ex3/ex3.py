def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    temp = []
    cache = {}
    result = []

    #need an array copy
    for temparr in arrays:
        temp.extend(temparr) #ah ha, hush that fuzz, add each array to the back of the list

    #let's loop the temp
    for number in temp:
        if number in cache:
            cache[number] +=1
        else:
            cache[number] = 1


        if cache[number] >= len(arrays):
            result.append(number)
        
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
