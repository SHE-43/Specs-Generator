from source_location_numbering_1 import s_l_d as sld
import csv, os, sys


for x,y in sld.items():
    print(  f"\n{x} has {y}\n"    )

# This will generate at random, but then you can save the shadow to a file which
#   can then be used to remember the src and locs we are going to be working with.
# Where can we save this without the help of pandas and numpy?

the_path = sys.path[0]

def path_creator(p, name):
    try:
        os.mkdir(os.path.join(p, name))
    except FileExistsError as f:
        print("This file/folder already exists.")
    else:
        print("Folder has been made")

path_creator(the_path, "network_main")      ;
path_creator(the_path, "shadow_file")       ;
print("\nThe path and it's folders\n")      ;
print(os.listdir(the_path))     ;
print("\nThe network path :\n")
network_path = os.path.join(the_path, "network_main")
# this is where the source and locations wil go.
print(network_path)
print(sld)

for src, loc in sld.items():
    path_1 = os.path.join(network_path, str(src))
    os.mkdir(path_1)
    for single_loc in loc:
        path_2 = os.path.join(path_1, str(single_loc))
        os.mkdir(path_2)
