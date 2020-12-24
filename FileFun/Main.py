import sys
import os
from collections import defaultdict

class FileSystem:
    def __init__(self, path, topn) -> None:
        self.path = path
        self.topn = topn
        super().__init__()

    # Function to insert element 
    def insert(self, list, pathSizeTuple): 
        i = 0
        if list[0]:
            # Searching for the position 
            for i in range(len(list)): 
                if list[i][1] < pathSizeTuple[1]: 
                    index = i 
                    break
            
            # Inserting n in the list 
            list = list[:i] + [pathSizeTuple] + list[i:self.topn] 
        else:
            list[0] = pathSizeTuple

        return list

    def subDirTotals(self, path, largestPathSizeTupleList, filter):
        count = 0
        size = 0
        try:
            for dirEntry in os.scandir(path):
                subName = os.path.join(path, dirEntry.name)
                if dirEntry.is_file():
                    if filter == '*' or dirEntry.name.endswith(filter):
                        count += 1
                        st_size = dirEntry.stat().st_size
                        size += st_size
                        largestPathSizeTupleList = self.insert(largestPathSizeTupleList, (subName, st_size))
                        size += 0
                else:
                    subCount, subSize, largestPathSizeTupleList = self.subDirTotals(subName, largestPathSizeTupleList, filter)
                    count += subCount
                    size += subSize
        except:
            pass
        return count, size, largestPathSizeTupleList            
    
    def dirInfo(self):
        for dirEntry in os.scandir(self.path):
            print(f'{dirEntry.path:<40} {dirEntry.name:<20} {dirEntry.is_dir():<8} {dirEntry.stat().st_size:>10}')

    def getDirectories(self, path):
        directories = [dir for dir in os.listdir(path) if not os.path.isfile(os.path.join(path, dir))]
        return sorted(directories)

    def getFiles(self, path):
        files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
        return files

    def listFilesAndDirs(self):
        directories = self.getDirectories(self.path)
        files = self.getFiles(self.path)

    def prettySize(size):
        newSize = size / (1024 * 1024)
        #newSize = '{0:,.2f}'.format(newSize)
        newSize = '{0:,.0f} MB'.format(newSize)
        return newSize

    def displayResults(self, results):
        for file, size in results:
            size = FileSystem.prettySize(size)
            print(f'{size:>15}   {file}')
    
fad = FileSystem('H:\\Python\\HelloWorld', 20)        
largest = [tuple()]
count, size, largest = fad.subDirTotals('C:\\', largest, '*')
fad.displayResults(largest)
print(f'Count: {count:,}, Size: {size:,}')

class DisplayModules:
    def displayModules():
        modules = defaultdict(list)
        for mod, val in sorted(sys.modules.items()):
            parts = mod.split('.', 1)
            if (len(parts) == 1):
                modules[parts[0]] = []
            else:
                modules[parts[0]].append(parts[1])
        for mod, values in modules.items():
            print(mod)        
            for val in values:
                print(f'    {val}')
#DisplayModules.displayModules()

