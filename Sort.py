import os, argparse, keyboard
from shutil import move
from pathlib import Path

def main():
    ## Arguments
    Arg = Arguments()
    location = Path(Arg["location"])
    
    # Absolute Path = Full Path
    # Relative Path = Part of a Path
    # print(Path.cwd()) -> current directory
    
    if IsLocation(location):
        return False
    
    while not keyboard.is_pressed("q"):
        #All of this is dangerous and I don't want crash
        #so let's use Exception Handling (try catch)
        try:
            if os.listdir(location):
                MoveFiles(GetFiles(location), location)
        except Exception as e:
            print("The error is:", e)
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

#Is it a file?
def IsFile(filepath) -> bool:
    if (Path(filepath).suffix == ''): return False
    if (Path.is_dir(filepath)): return False
    return True

#Returns list of all files in the directory
def Runls(location) -> list:
    return os.listdir(location)

#Returns if the suffix exists in the file extension
def HasThisSuffix(File,Suffix) -> bool:
    Ext = File.split(".")[-1]
    return Suffix in Ext

#Returns All Files in the directory
def GetFiles(location) -> list:
    Files = []
    for File in Runls(location):
        Filepath = Path(f'{Path.as_posix(location)}/{File}')
        if IsFile(Filepath) and not HasThisSuffix(File,"crdownload"):
            Files.append(File)
    return Files

#Moves File from old location to a new location
def MoveFiles(Files, location) -> None:
    for File in Files:
        OldLocation = f'{Path.as_posix(location)}/{File}'
        Ext = File.split(".")[-1]
        if Ext != '':
            NewLocation = f'{Path.as_posix(location)}/{Ext}/{File}'
        else:
            NewLocation = f'{Path.as_posix(location)}/Others/{File}'
        if not Path(os.path.dirname(NewLocation)).exists():
            Path.mkdir(os.path.dirname(NewLocation))
        move(OldLocation,NewLocation)

#Define as script
if __name__ == "__main__":
    main()
