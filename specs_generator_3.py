# 
# this creates a CSV shadow file for saving names.

# source location freq day time start_date


import csv, os, sys, random, datetime

path = sys.path[0] + "/network_main"

sources = os.listdir(path)

def L(k):return int(k)

sorted_sources = sorted(sources, key = L)

dict_src_loc = dict()

for source in sources:
    src_path = path + "/" + source
    locs_in_src = os.listdir(src_path)

# Either, you can place a specs file in each location folder or
# You could create a shadow file pointing at all locations and their specs.
# Or both.

days = [datetime.datetime.strftime(datetime.datetime(2020,10,x), "%A" ) for x in range(5,12)]


def random_specs(src, loc):
    freq = random.choice(["Monthly", "Weekly", "Daily" ])
    
    if freq == "Monthly":
        day = random.choice(days);
        which_day = [str(x)+y for x,y in zip( range(1,4), ["st", "nd", "rd"])        ]
        DL_day = random.choice(which_day) + " " + day
        time = datetime.datetime(1970,1,1, random.choice([x for x in range(1,12)]),0,0)
        start_date = datetime.datetime(random.choice([2019,2020]), random.choice([1,2,3,4,5,6]), random.choice([x for x in range(1,27)]) )
        
    elif freq == "Weekly":
        day = random.choice(days);
        DL_day = day
        time = datetime.datetime(1970,1,1, random.choice([x for x in range(1,12)]),0,0)
        start_date = datetime.datetime(2020, random.choice([1,2,3,4]), random.choice([x for x in range(1,27)]) )
        
    else:
        DL_day = "Any"
        time = datetime.datetime(1970,1,1, random.choice([x for x in range(1,12)]),0,0)
        start_date = datetime.datetime(2020, random.choice([6,7,8]), random.choice([x for x in range(1,27)]) )


    dictionary = {"Source": src, "Location": loc, "Freq": freq, "DL_day": DL_day, "time": time, "start_date": start_date, "perfection": random.choice(["Perfect", "Imperfect"])} 
    return dictionary



for src in sources:     # go over each source ID
    loc_list_path = path + "/" + src # the path is the network_main folder # we combine that path with the source ID
    loc_list = os.listdir(loc_list_path) # the list of all location IDs in that source folder.

    for loc in loc_list:    # go over each location ID in that source folder
        loc_path = loc_list_path + "/" + loc    # create path for each location.
        specs = random_specs(src, loc)    # use our method to create specs for that source and location.
        specs_file_path_name = loc_path + "/" + f"{src}_{loc}_specs.txt"
        with open(specs_file_path_name, "w") as f:  # open a writable file in location folder.
            for k,i in specs.items():   # go over the specs dictionary made using method, 
                f.write(  f"{k} = {i}\n"  )     # write in each specs file, the specs we need.

                            
            
        






    


