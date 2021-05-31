class Singleton(object):
    __instance = None
    def __init__(self):
        if Singleton.__instance != None:
            return 'Singleton class'
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

#s = Singleton()
#print(s)
#s = Singleton.getInstance()
#print(s)
#s = Singleton.getInstance()
#print(s)

from abc import ABC, abstractmethod
class abstractliving(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def communicate(self):
        pass

    def cansee(self):
        print('i can see')

class human(abstractliving):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    def communicate(self):
        print('humans can talk')

human = human('man', 'earth')
human.communicate()
print(human.name)
