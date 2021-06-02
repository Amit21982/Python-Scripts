
from abc import ABC, abstractmethod
import time
class FileSystemBase(ABC):
    '''
    class defining common functions for file and directory
    '''
    def __init__(self, name:str = None, permissions: str=None, parentdir=None):
        self.parent = parentdir
        self.name = name
        self.created = time.time()
        self.updated = time.time()
        self.permission = permissions

    @abstractmethod
    def getsize(self):
        pass

    @abstractmethod
    def getcontent(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    def change_permission(self, permission:str) -> None:
        self.permission=permission

    def get_file_properties(self):
        return ("created {} - file updated {} - file {} ".format(self.created, self.updated, self.permission))

class Directory(FileSystemBase):
    def __init__(self, name, parent, permission):
        super().__init__(name, parent, permission)
        #since file has file lists
        self.filelist = []
        self.subdir = []

    def create(self):
        pass

    def movedir(self):
        """
        function will move items from one dirctory to other
        """
        pass
    def copydir(self):
        """
        function will copy items from one dirctory to other
        """
        pass

    def createsubdir(self, subdir):
        if subdir not in self.subdir:
            print('add sub dirrctor')
            self.subdir.append(subdir)
        else:
            return 'Directory not found'

    def deletsubdir(self, subdir):
        if subdir in self.subdir:
            self.subdir.remove(subdir)

    def listsubdir(self):
         return self.subdir

    def delete(self):
        """
        Function will delete the object and return None
        """
        if self.dir in self.filelist:
            self.remove(self.dir)

    def getsize(self):
        """
        get all files and compute its size
        """
        size =0
        for file in self.filelist:
            size += file.size
        return size

    def createfile(self, name):
        if name not in self.filelist:
            self.filelist.append(name)
            return 'File created in dir'
        else:
            return 'File with same name alread exist. Choose a different name'

    def getcontent(self):
        """
        Will list all the contents in the directory
        """
        filelist=[]
        if len(self.filelist) == 0:
            return "empty directory"
        else:
            for file in self.filelist:
                filelist.append(file)
        return filelist

class File(FileSystemBase):
    def __init__(self, name, parent, permission,type):
        super().__init__(name, parent, permission)
        parent.createfile(name)
        self.filecontent = None
        self.type = type
        self.permission = permission

    def write(self,content, mode):
        if self.permission == 'w':
            if mode == 'a':
                self.filecontent += content
            if mode == 'w':
                self.filecontent = content
        else:
            return 'file is read only'

    def create(self, parent, filename):
        return parent.createfile(filename)

    def getcontent(self):
        return self.filecontent

    def getsize(self):
        return len(self.filecontent)

    def delete(self, parent, content):
        parent.delete()

def test_file_operation():
    print('*'*100)
    print("File operations")
    print('*'*100)
    print('Creating a root directory')
    dirobj = Directory('rootdir', None, 'w')
    print(dirobj.get_file_properties())

    print('Creating a file in root directory')
    fileobj= File('testfile', dirobj, 'w', 'txt')

    print('getting content of root directory')
    print(dirobj.getcontent())

    print('write in files')
    fileobj.write('in memory file', 'w')

    print('read from files')
    print("File content is -> " + fileobj.getcontent())

    print('append in files')
    fileobj.write(' appended new content', 'a')

    print('read from files')
    print("File updated content is -> " + fileobj.getcontent())
    print('*'*100)

def test_dir_operation():
    print("Directory operations")
    print('*'*100)
    print('Creating a root directory')
    dirobj = Directory('rootdir', None, 'w')

    print('Get dir properties')
    print(dirobj.get_file_properties())

    print('Creating a sub-root directory')
    subdirobj = Directory('sub-rootdir', None, 'w')
    dirobj.createsubdir(subdirobj)

    print('Creating a sub-root1 directory')
    subdirobj1 = Directory('sub-rootdir1', None, 'w')
    dirobj.createsubdir(subdirobj1)

    print('List contents')
    subdirlist = dirobj.listsubdir()
    for dir in subdirlist:
        print(dir.name)

    print('Creating a file in sub-root1 directory')
    fileobj= File('testfile1', subdirobj1, 'w', 'txt')

    print('Creating a file in sub-root directory')
    fileobj= File('testfile2', subdirobj, 'w', 'txt')

    print('List contents along with files')
    subdirlist = dirobj.listsubdir()
    for dir in subdirlist:
        print("Directory --> "  + dir.name)
        if dir.getcontent() != None:
            for file in dir.getcontent():
                print("         files in directory   " + file)
    print('#'*100)

test_file_operation()
