import os, argparse
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
        location = IsLocation(location)
        Folders = GetFolders(location)
        for Folder in Folders:
            print(GetFolders(Folder))
            
    except Exception as e:
        print("The Error is: ", e.args)

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

#Is it really file?
def IsFile(filepath):
    if (Path(filepath).suffix == ''): return False
    if (Path.is_dir(filepath)): return False
    return True

# GetFolders
def GetFolders(location):
    Folders = []
    Filelist = os.listdir(location)
    if Filelist == []:
        return Folders
    for File in Filelist:
        filepath = Path(Path.as_posix(location)+ "/" + File)
        if not(IsFile(filepath)):
            Folders.append(filepath)
    return Folders

#Define as script
if __name__ == "__main__":
    main()
