###########################
# 6.0002 Problem Set 1a: Space Cows
# Name: Tuvshin-Erdene 23b1num0869
# Collaborators:
# Time:

import time

from ps4_partition import get_partitions

# ================================
# Part A: Transporting Space Cows
# ================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    animal_dict = {}
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, weight = line.split(',')
                animal_dict[name.strip()] = int(weight.strip())
        return animal_dict
    except FileNotFoundError:
        return "Error file was not found"
    except ValueError:
        return "error check your file format"


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    trips = []
    transported_cows = set()
    while len(transported_cows) < len(cows):
        current_trip = []
        current_weight = 0
        for name , weight in sorted_cows:
            if name not in transported_cows and (current_weight+weight) <= limit:
                current_trip.append(name)
                current_weight += weight
                transported_cows.add(name)
        trips.append(current_trip)
    return trips
            




# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_partition = None
    min_trips  = len(cows) + 1
    for partition in get_partitions(list(cows.keys())):
        is_valid = True
        for trip in partition:
            trip_weight = sum(cows[cow] for cow in trip)
            if trip_weight > limit:
                is_valid = False
                break
        if is_valid:
            if len(partition) < min_trips:
                min_trips = len(partition)
                best_partition = partition
    
    return best_partition




# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps4_cow_data.txt")


    print("running greedy algorithm")
    start = time.time()
    result = greedy_cow_transport(cows,10)
    end = time.time()
    print(result)
    print(f"total {len(result)} trips")
    print(f"total time spent {(end - start)}")

    print("running brute force algorithm")
    start = time.time()
    result = brute_force_cow_transport(cows,10)
    end = time.time()
    print(result)
    print(f"total {len(result)} trips")
    print(f"total time spent {(end - start)}")

compare_cow_transport_algorithms()
    
