import sys
import os
import random

# We are going to start with 3 sources however this is now based on input only.

number_of_sources = 5; # Input for number of sources needed
start,end = 111,1432; # Starting number and ending number for source IDs.
src_list = []

src_gen = lambda x,y : random.randint(x,y)


for x in range(number_of_sources):
    src_number = src_gen(start, end)
    b = True
    while b:
        if src_number not in src_list:
            src_list.append(src_number);
            b = False;
        else:
            src_number = src_gen(start, end)
            
# Now, let's generate locations for these sources.
min_locs, max_locs = 5, 15;
src_loc_dict = dict();

for src in src_list:
    number_of_locations = src_gen(min_locs, max_locs);
    one_or_two = random.randint(1,2);
    if one_or_two == 2 and number_of_locations == 5:
        number_of_locations += 2;
    o_o_t = one_or_two;
    n_o_l = number_of_locations
    list_of_locations = [x for x in range(o_o_t, n_o_l)]

    src_loc_dict[src] = list_of_locations


s_l_d = src_loc_dict;

# import this to the next file.


















