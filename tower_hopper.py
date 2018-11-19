# Given an array of integers where each element represents the max number of steps that can be made forward from that element.
# Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, then cannot move through that element.


# The idea here is to find the minimum number of hops to reach all the indexes starting from zero to n. Then return value for index n.
# To find minimum number of hops for i'th node we can use the previously computed results for all the nodes from which we can reach ith node.
# Then take minimum of all those values.
# refer - https://www.youtube.com/watch?v=cETfFsSTGJI

def min_hops(towers) :
    hops = [None] * len(towers)
    hops[0] = 0
    for i in range(1, len(towers)) :
        min_hops = 10000
        for j in range(i) :
            if j + towers[j] >= i :
                min_hops = min(min_hops, hops[j] + 1)
        hops[i] = min_hops

    return hops[len(towers)-1]

towers = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
towers= [0, 1]
print min_hops(towers)
