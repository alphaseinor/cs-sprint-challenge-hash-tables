# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for path in files:
        name = path.split('/')[-1]
        if name not in cache:
            cache[name] = [path]
        else:
            cache[name].append(path)

    for query in queries:
        if query in cache:
            #duplicates?
            for path in cache[query]:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
