import sys, os, random;
from datetime import datetime, timedelta;

d1 = datetime(2020,11,1, 0, 43, 43);
d2 = datetime(year = 2020, month = 11, day = 7, hour = 0,minute= 43, second=44);
t1 = d2 - d1;

# Start looping over all locations.

path = sys.path[0] + "/" + "network_main";
sources = [src for src in os.listdir(path)];
sources_with_paths = [(path + "/" + src) for src in sources]; # to be used in the method.

src_loc_dict = dict();

for x in sources_with_paths:
    locs = os.listdir(x);
    src_loc_dict[x] = locs;

print("\n\nThe dict of the source path and list of location IDs.\n");

# This method takes a source path and returns paths of all locations in it.
def locs_with_paths_list(src_path) -> "Source path" : 
    loc_path_list = [];    
    for location in os.listdir(src_path):
        path = src_path + "/" + location;
        loc_path_list.append(path);
    loc_path_list = sorted(loc_path_list, key = lambda k: int(  k.split("/")[-1]  ));
    return loc_path_list # returns the list of locations with paths.

print("\nThe method that creates location paths for the source it takes in");

src_path_to_list_of_loc_paths_dict = dict();

for src_path in sources_with_paths:
    loc_paths_list = locs_with_paths_list(src_path)
    src_path_to_list_of_loc_paths_dict[src_path] = loc_paths_list

print("\nA dictionary that has source path and list of location paths...\n");
for x,y in src_path_to_list_of_loc_paths_dict.items():
    print("Source path")
    print(x)
    print("\nList of location paths below")
    print(y)
    print("\n\n")

src_chosen = sources_with_paths[0]; # 1270 because I know.
locs_chosen = locs_with_paths_list(sources_with_paths[0]); # has paths to all locations.

print("\n\nThe chosen src and loc for chosen source.\n\n");

# This method reads specs from location path.
def specs_reader(loc_path) -> "Location path." : # reads and turns to raw.
    file = os.listdir(loc_path)[0];
    path_of_file = loc_path + "/" + file;
    with open(path_of_file, 'r') as f:
        a = f.readlines();
    return a; # returns raw specs.

list_of_specs = specs_reader(locs_chosen[0]); # 1270_1

print("\n\nList above and dict below\n\n")

# This method converts that list to a dictionary.
def spec_to_dict(specs_list) -> "Raw specs list" : # takes in raw list of specs.
    list_refined = [x[0:-1] for x in specs_list ]
    dict_refined = dict(); 
    for spec in list_refined:
        single_spec = spec.split("=");
        a,b = single_spec[0], single_spec[1];
        a = a.strip();
        b = b.strip();
        dict_refined[a] = b;
    return dict_refined; # returns refined dictionary of specs.

print(spec_to_dict(list_of_specs))

# This method creates a dictionary that has location path as key and specs list as value.

def loc_to_specs_dict_gen(src_path):

    # return a dictionary of src,loc to specs of it.
    
    locs_with_paths = locs_with_paths_list(src_path)
    loc_path_to_specs_dict = dict()

    for loc_path in locs_with_paths:
        raw_specs = specs_reader(loc_path);
        specs_dict = spec_to_dict(raw_specs);
        loc_number = loc_path.split("/")[-1]
        src_number = loc_path.split("/")[-2]
        src_loc_tuple = (src_number, loc_number)
        loc_path_to_specs_dict[src_loc_tuple] = specs_dict

    return loc_path_to_specs_dict

print("\n\nMethod that gives tuple as key and specs dict as value...\n\n")

for x,y in loc_to_specs_dict_gen(sources_with_paths[1]).items():    
    print(x);
    print("\n");
    print(y);
    print("\n"); print("\n");


specs = spec_to_dict(list_of_specs);
print(specs)

# Now, let's generate files.

# This is the one we'gve been waiting for.
# All is well and done.


"""
{'Source': '1270', 'Location': '1', 'Freq': 'Daily', 'DL_day': 'Any', 'time': '1970-01-01 01:00:00',
'start_date': '2020-06-13 00:00:00', 'perfection': 'Perfect'}
"""






















"""'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold',
'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp',
'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min',
'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime',
'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname',
'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']"""
