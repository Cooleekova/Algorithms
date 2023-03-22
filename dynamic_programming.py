""" Dynamic programming is a computer programming technique 
where an algorithmic problem is first broken down into sub-problems, 
the results are saved, 
and then the sub-problems are optimized to find the overall solution 
— which usually has to do with finding the maximum and minimum range of the algorithmic query """


# At the moment your house is 100 square meters. 
# The area that your things occupy is 50 square meters. 
# Your new apartment is 40 square meters 
# and you want your stuff to occupy 20 square meters at most.
total_area = 2000
# Your goal is to maximize the value on the 20 square meters.
# Source:
# https://towardsdatascience.com/choosing-fast-with-dynamic-programming-b6916da543f4



# Step 1. Create a dictionary with items and area/value they contain.
# Step 2. Create area and value lists from the dictionary.
# Step 3. Use these lists to build the memoization table.
# Step 4. Get the items included in the last row of the memoization table.


# List your items specifying the area (in square decimeters) 
# and also the value items add to your life (on a scale from 0 to 100).
stuffdict = {'couch_s':(300,75), 
             'couch_b':(500,80), 
             'bed':(400,100), 
             'closet':(200,50), 
             'bed_s':(200,40), 
             'desk':(200,70), 
             'table':(300,80),
             'tv_table':(200,30),
             'armchair':(100,30),
             'bookshelf':(200,60), 
             'cabinet':(150,20),
             'game_table':(150,30),
             'hammock':(250,45),
             'diner_table_with_chairs':(250,70),
             'stools':(150,30),
             'mirror':(100,20),
             'instrument':(300,70),
             'plant_1':(25,10),
             'plant_2':(30,20),
             'plant_3':(45,25),
             'sideboard':(175,30),
             'chest_of_drawers':(25,40),
             'guest_bed':(250,40),
             'standing_lamp':(20,30), 
             'garbage_can':(30, 35), 
             'bar_with_stools':(200,40), 
             'bike_stand':(100,80),
             'chest':(150,25),
             'heater':(100,25)
            }


# create area and value lists 
def get_area_and_value(stuffdict):
    area = []
    value = []
    
    for item in stuffdict:
        area.append(stuffdict[item][0])
        value.append(stuffdict[item][1])
        
    return area, value


# build a table
# You need the total area and the total number of items n. 
# The table has n+1 rows and total area+1 columns. 
# Start on the first row with zero items and calculate the value for every cell.
def get_table(area, value, total_area=total_area, n=len(stuffdict)):
    # The table has n+1 rows and total area+1 columns. 
    table = [[0 for a in range(total_area+1)]
        for i in range(n+1)]
    # fill every cell of the table
    for i in range(n+1):
        for a in range(total_area+1):
            # when the area or the number of items is zero, the value is zero
            if i == 0 or a == 0:
                table[i][a] = 0
            # when the area of the current item (area[i-1]) 
            # is smaller or equal to the area of the cell (a), 
            # calculate the value of the cell
            elif area[i-1] <= a:
                # choose the maximum between 
                # the value of the current item (value[i-1]) plus the value of the previous row 
                # and the current area minus the area of the current item (table[i-1][a-area[i-1]])
                # and the value of the previous row with the area of the current cell table[i-1][a]
                table[i][a] = max(value[i-1] + table[i-1][a-area[i-1]], table[i-1][a])
            # if the area of the cell (a) is smaller 
            # than the area of the current item (area[i-1]) 
            # set the value of the cell equal 
            # to the value of the previous row with the same area (table[i-1][a])
            else:
                table[i][a] = table[i-1][a]       
    return table



# get the solution
def get_selected_items_list(total_area=total_area, n=len(stuffdict)):
    area, value = get_area_and_value(stuffdict)
    table = get_table(area, value)
    # max value is stored in the lowest right cell of the table
    maximum_value = table[n][total_area]
    # at first all of the area is available
    available_area = total_area
    # create variable to count already used area
    used_area = 0
    # create a list to store chosen items' value and area
    items_list = []
    
    # start to search for items in the table
    for i in range(n, 0, -1):
        # when max_value is zero, stop searching
        if maximum_value <= 0:
            break
        # in the starting point with max value do nothing and go ahead
        if maximum_value == table[i-1][available_area]:
            continue
        # add item to the list,
        # decrease available area by item area
        # and increase used area counter,
        # decrease max value by item value
        else:
            items_list.append((area[i-1], value[i-1]))
            used_area += area[i-1]
            maximum_value -= value[i-1]
            available_area -= area[i-1]
    
    # create a list to store chosen items names
    selected_stuff = []
    # check every item in the list
    for search in items_list:
        # compare it to the dict values
        for key, value in stuffdict.items():
            # when the value in dict is equal to search
            if value == search:
                # add dict key to the final list
                selected_stuff.append(key)
    # watch out!!!!
    # this code isn't perfect,
    # it also returns duplicates 
    # (items with the same area and value pair)!
    if sum([stuffdict[item][0] for item in selected_stuff]) > total_area:
        raise BaseException("Duplicates in the list!")
    return f"Used area: {used_area / 100} square meters, \nSelected items: {len(selected_stuff)}, \n{selected_stuff}"


# try it out
print(get_selected_items_list())
