import random

class markov(object):
    def __init__(self):
        self.__fileName = ''
        self.__count = 0
        self.__list = []
    
    def seedFile(self,fileName):
        self.__count = 0
        with open(fileName) as f:
            self.__list = f.read().split()
            self.__count = len(self.__list)
        if self.__count == 0:
            error('seed file not loaded or is empty')
    
    def seedString(self,words):
        self.__count = 0
        self.__list = words.split()
        self.__count = len(self.__list)
    
    def seed(self,items):
        self.__count = 0
        self.__list = items
        self.__count = len(self.__list)
    
    def genChain(self,length,seedLen=1):
        if self.__count == 0:
            error('seed file not loaded or seed file is empty')
        if self.__count < seedLen:
            error('too few words in seed file')
        seedIndex = random.randint(0,self.__count - (seedLen+1))
        
        seed = self.__list[seedIndex:seedIndex+seedLen]
        return self.genChainFromSeed(length,seed)
    
    def genChainFromSeed(self,length,seed):
        #do this so we don't modify the original seed in the calling function
        items = seed
        for i in range(length-len(items)):
            seed.append(self.__getNext(items[i:]))
        return items
    
    def __getNext(self,items):
        indicies = []
        num = len(items)
        stop = self.__count
        for i in range(num,stop):
            if self.__list[i-num:i] == items:
                indicies.append(i)
        count = len(indicies)
        if count == 0:
            return ''
        choice = random.randint(0,count-1)
        return self.__list[indicies[choice]]
