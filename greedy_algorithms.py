"""A greedy algorithm is an approach for solving a problem 
by selecting the best option available at the moment. 
It doesn't worry whether the current best result will bring the overall optimal result. 
The algorithm never reverses the earlier decision even if the choice is wrong."""

# example of greedy algorithm:

"""The set cover problem
is a classical question in combinatorics, 
computer science, operations research, and complexity theory."""

# Consider having a radio program which must be performed in several regions.
# The task is to find a set of radio stations which will cover all the regions.

# a list of all regions needed to be covered
regions_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# a list of radio stations and regions they cover
stations = {}
stations['k-four'] = set(['nv', 'ut'])
stations['k-two'] = set(['wa', 'id', 'mt'])
stations['k-three'] = set(['or', 'nv', 'ca'])
stations['k-five'] = set(['ca', 'az'])
stations['k-one'] = set(['id', 'nv', 'ut'])

# the final list of stations = solution for the problem
final_list_of_stations = set()

# search for radio stations until there are uncovered regions
while regions_needed:
    # using greedy approach find optimal radio station 
    # - the one which covers more regions than others
    optimal_station = None
    regions_covered_by_optimal_station = set()
    # find which of needed regions are covered by station
    # use sets intersection syntax
    for station, regions_for_station in stations.items():
        covered_regions = regions_needed & regions_for_station
        # choose from the list of stations the one which covers the biggest quantity of regions
        # save it in optimal station variable 
        if len(covered_regions) > len(regions_covered_by_optimal_station):
            optimal_station = station
            regions_covered_by_optimal_station = covered_regions
    # add optimal station to the final stations list
    final_list_of_stations.add(optimal_station)
    # remove covered regions from the search list and repeat the algorithm
    regions_needed -= regions_covered_by_optimal_station
    
# print the solution
print(f'Final list of stations: {final_list_of_stations}')
