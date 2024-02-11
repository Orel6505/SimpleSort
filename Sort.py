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
        if IsLocation(location):
            raise ValueError("Location is invalid")
        Folders = []
        for Folder in GetFolders(location):
            Folders.append(Path.as_posix(Folder))
        print(Folders)
        Files = []
        for File in GetFiles(location):
            if Path.as_posix(File).endswith("exe"):
                Files.append(Path.as_posix(File))
        print(Files)
    except Exception as e:
        print("Error:", e)

#Pass All Arguments
def Arguments():
    parser = argparse.ArgumentParser(description="Just a simple sorting script",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-l", "--location", type=str, nargs='?', default=Path.home()/"Downloads", help="Custom location to sort, default is Downloads folder")
    args = vars(parser.parse_args())
    return args

#Is the location real?
def IsLocation(location):
    if not Path(location).is_absolute(): return True
    if not Path(location).exists(): return True
    return False

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
        filepath = Path(Path.as_posix(location) + "/" + File)
        if not(IsFile(filepath)):
            Folders.append(Path(filepath))
    return Folders

def GetFiles(location):
    Files = []
    Filelist = os.listdir(location)
    if Filelist == []:
        return Files
    for File in Filelist:
        filepath = Path(Path.as_posix(location) + "/" + File)
        if IsFile(filepath):
            Files.append(Path(filepath))
    return Files

#Define as script
if __name__ == "__main__":
    main()
