import os, argparse, keyboard, time
from pathlib import Path

def main():
    ## Arguments
    Arg = Arguments()
    location = Arg["location"]
    
    # Absolute Path = Full Path
    # Relative Path = Part of a Path
    # print(Path.cwd()) -> current directory
    
    if IsLocation(location):
        return False
    
    while not keyboard.is_pressed("q"):
        #All of this is dangerous and I don't want crash
        #so let's use Exception Handling (try catch)
        try:
            if GetFiles(location) != []: #Temporarly
                print(GetFolders(location))
                print(GetFilesBySuffix(location,"exe"))
        except Exception as e:
            print("Error:", e)
            break

#Pass All Arguments
def Arguments() -> dict:
    parser = argparse.ArgumentParser(description="Just another simple sorting script",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-l", "--location", type=str, nargs='?', default=Path.home()/"Downloads", help="Custom location to sort, default is Downloads folder")
    args = vars(parser.parse_args())
    return args

#Is the location real?
def IsLocation(location) -> bool:
    if Path(location).is_absolute(): return False
    if Path(location).exists(): return False
    return True

#Is it really file?
def IsFile(filepath) -> bool:
    if (Path(filepath).suffix == ''): return False
    if (Path.is_dir(filepath)): return False
    return True

#Returns list of all files in the directory
def Runls(location) -> list:
    return os.listdir(location)

#Returns Path object contains location and file
def FilePathCreator(location,File) -> Path:
    return Path(Path.as_posix(location) + "/" + File)
                
# Returns all Folder in the directory
def GetFolders(location) -> list:
    Folders = []
    for File in Runls(location):
        Filepath = FilePathCreator(location,File)
        if not(IsFile(Filepath)):
            Folders.append(File)
    return Folders

#Returns All Files in the directory
def GetFiles(location) -> list:
    Files = []
    for File in Runls(location):
        Filepath = FilePathCreator(location,File)
        if IsFile(Filepath):
            Files.append(File)
    return Files

#Returns a list that contains all the files with the extension name
def GetFilesBySuffix(location, suffix) -> list:
    Files = []
    for File in Runls(location):
        if File.endswith(suffix):
            Files.append(File)
    return Files

#Define as script
if __name__ == "__main__":
    main()
