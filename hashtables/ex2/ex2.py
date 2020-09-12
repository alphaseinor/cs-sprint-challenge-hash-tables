#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    route = [None] * length

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    #so the start is going to be none from the data given
    current = cache['NONE']

    for i in range(length):
        route[i] = current
        current = cache[current] #move current to the next



    return route
