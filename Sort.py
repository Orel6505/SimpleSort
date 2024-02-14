import os, argparse, keyboard
from pathlib import Path

def main():
    ## Arguments
    Arg = Arguments()
    location = Arg["location"]
    
    # Absolute Path = Full Path
    # Relative Path = Part of a Path
    # print(Path.cwd()) -> Prints current directory
    
    if IsLocation(location):
        return False
    
    while True:
        #All of this is dangerous and I don't want crash
        #so let's use Exception Handling (try catch)
        try:
            if keyboard.read_key() == "q":
                print("You pressed p")
                break
            print(GetFolders(location))
            print(GetFilesBySuffix(location,"exe"))
        except Exception as e:
            print("Error:", e)

#Pass All Arguments
def Arguments():
    parser = argparse.ArgumentParser(description="Just a simple sorting script",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-l", "--location", type=str, nargs='?', default=Path.home()/"Downloads", help="Custom location to sort, default is Downloads folder")
    args = vars(parser.parse_args())
    return args

#Is the location real?
def IsLocation(location) -> bool:
    if Path(location).is_absolute(): return False
    if Path(location).exists(): return False
    return False

#Is it really file?
def IsFile(filepath) -> bool:
    if (Path(filepath).suffix == ''): return False
    if (Path.is_dir(filepath)): return False
    return True

#Returns list of all files in the directory
def Runls(location) -> list:
    Filelist = os.listdir(location)
    return Filelist

def FilePath(location,File) -> Path:
    return Path(Path.as_posix(location) + "/" + File)
                
# GetFolders
def GetFolders(location) -> list:
    Folders = []
    Filelist = Runls(location)
    for File in Filelist:
        filepath = FilePath(location,File)
        if not(IsFile(filepath)):
            Folders.append(Path.as_posix(filepath))
    return Folders

#Get All Files in the directory
def GetFiles(location) -> list:
    Files = []
    Filelist = Runls(location)
    for File in Filelist:
        filepath = FilePath(location,File)
        if IsFile(filepath):
            Files.append(Path.as_posix(File))
    return Files

def GetFilesBySuffix(location, suffix) -> list:
    Files = []
    for File in GetFiles(location):
        if Path.as_posix(File).endswith(suffix):
            Files.append(Path.as_posix(File))
    return Files

#Define as script
if __name__ == "__main__":
    main()
