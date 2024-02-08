import os, argparse
from pathlib import Path

def main():
    ## Arguments
    SArg = Arguments()
    
    location = SArg["location"]
    guess = SArg["guess"]
    
    # Absolute Path = Full Path
    # Relative Path = Part of a Path
    # print(Path.cwd()) -> Prints current directory
    
    #All of this is dangerous and I don't want crash, so let's use try
    try:
        location = CheckLocation(location)
    except Exception as e:
        print(e.args)
    finally:
        print("Done")
        
#Pass All Arguments
def Arguments():
    parser = argparse.ArgumentParser(description="Just a simple sorting script",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-l", "--location", type=str, nargs='?', default=Path.home()/"Downloads", help="Custom location to sort, default is Downloads folder")
    parser.add_argument("-g", "--guess", type=bool, nargs='?', default=False, help="Guess The location")
    args = vars(parser.parse_args())
    print(args)
    return args

#Is the location real?
def CheckLocation(location):
    if (not Path.is_absolute(location)):
        os.path.abspath(location)
        if(not Path.exists(location)):
            return None
    return location
        
if __name__ == "__main__":
    main() #define as script
