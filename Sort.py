import os, argparse, json
from pathlib import Path

def main():
    ## Arguments
    Arg = Arguments()
    
    location = Arg["location"]
    
    # Absolute Path = Full Path
    # Relative Path = Part of a Path
    # print(Path.cwd()) -> Prints current directory
    
    #All of this is dangerous and I don't want crash, so let's use try
    try:
        location = Path(IsLocation(location))
    except Exception as e:
        print("The Error is: ", e.args)
    GetAllFiles(location)

#Pass All Arguments
def Arguments():
    parser = argparse.ArgumentParser(description="Just a simple sorting script",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-l", "--location", type=str, nargs='?', default=Path.home()/"Downloads", help="Custom location to sort, default is Downloads folder")
    args = vars(parser.parse_args())
    return args

#Is the location real?
def IsLocation(location):
    if (not Path.is_absolute(location)):
        os.path.abspath(location)
        if(not Path.exists(location)):
            return None
    return location

def IsFile(filepath):
    if not(os.path.getsize(filepath) or os.path.getsize(filepath)==0): return False
    if (Path(filepath).suffix == '' and Path.is_dir(filepath)): return False
    return True

#Creates Object File for all files in this directory and sub directories
def GetAllFiles(location):
    for file in os.listdir(location):
        filepath = location/file
        if (IsFile(filepath)):
            print("#move files to desired location")
        else:
            print("#move folder to desired location")

#Define as script
if __name__ == "__main__":
    main()
