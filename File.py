import os
from pathlib import Path

class File():
    def __init__(self, filepath):
        filename=os.path.basename(filepath)
        filesize=os.path.getsize(filepath)
        is_accessible=File.IsAccessible(filepath)
            
    #Checks if read permission
    def IsAccessible(filepath):
        raise NotImplementedError