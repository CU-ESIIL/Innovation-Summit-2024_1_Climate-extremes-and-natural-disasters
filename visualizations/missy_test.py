from data_loader import *
import subprocess

# copies file from a cyverse path to your local data dir 
def copy_cyverse_file_to_personal(fp):
    out = subprocess.run(["gocmd", "cp", fp, "."])    
    return out

# copies file from a cyverse path to our repo data dir
def copy_cyverse_file_to_group(fp):
    dest = "/Innovation-Summit-2024_1_Climate-extremes-and-natural-disasters/data"
    out = subprocess.run(["gocmd", "cp", fp, dest])    
    return out 


