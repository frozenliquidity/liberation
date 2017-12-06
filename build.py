import os
import os.path

import shutil
from distutils.dir_util import copy_tree

def get_mpmission_dir():
	if 'ARMA3_DIR' in os.environ:
		base_dir = os.environ['ARMA3_DIR']
	else:
		base_dir = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
	return os.path.join(base_dir, 'MPMissions')

def get_subdirs(dirname):
    d = dirname
    return [os.path.join(d, o) for o in os.listdir(d) 
            if os.path.isdir(os.path.join(d,o))]

def find_all_mission_folders():
    mission_folders = get_subdirs(os.path.join(os.getcwd(), 'Missionbasefiles'))
    mission_folders = [os.path.split(x)[-1] for x in mission_folders if x[0] != '.']
    return mission_folders

def clean(mission_folders):
    for dirname in mission_folders:
        if dirname[0] != '.':
            clean_dir = os.path.abspath(os.path.join(get_mpmission_dir(), dirname))
            if os.path.exists(clean_dir):
                print("Removing output build found in: {}".format(clean_dir))
                shutil.rmtree(clean_dir)


def build(mission_folders):
		
    for dirname in mission_folders:
        src = os.path.join(os.getcwd(), 'Missionbasefiles', dirname)
        dest = os.path.abspath(os.path.join(get_mpmission_dir(), dirname))
        shutil.copytree(src, dest)
        src = os.path.join(os.getcwd(), 'Missionframework')
        copy_tree(src, dest)
    

def main():
    mission_folders = find_all_mission_folders()
    clean(mission_folders)
    build(mission_folders)

if __name__ == '__main__':
    main()
	
