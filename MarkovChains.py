import random

class markov(object):
    def __init__(self):
        self.__count = 0
        self.__list = []
    
    def sourceFile(self,fileName,words=True):
        self.__count = 0
        with open(fileName) as f:
            if words:
                self.source(f.read().split())
            else:
                self.source(f.read())
        if self.__count == 0:
            raise Exception('source not loaded')
    
    def source(self,items):
        self.__list = items
        self.__count = len(self.__list)
        if self.__count == 0:
            raise Exception('source is empty')
    
    def genChain(self,length,seedLen=1):
        if self.__count == 0:
            raise Exception('source not loaded')
        if self.__count < seedLen:
            raise Exception('too few items in source list')
        seedIndex = random.randint(0,self.__count - (seedLen+1))
        
        seed = self.__list[seedIndex:seedIndex+seedLen]
        return self.genChainFromSeed(length,seed)
    
    def genChainFromSeed(self,length,seed):
        #do this so we don't modify the original seed in the calling function
        #doing this actually might not accomplish anything
        #todo: determine if this actually does anything
        items = seed
        for i in xrange(length-len(items)):
            try:
                items.append(self.__getNext(items[i:]))
            except:
                items += self.__getNext(items[i:])
        return items
    
    def __getNext(self,items):
        indicies = []
        num = len(items)
        stop = self.__count
        for i in xrange(num,stop):
            if self.__list[i-num:i] == items:
                indicies.append(i)
        count = len(indicies)
        if count == 0:
            return ''
        choice = random.randint(0,count-1)
        return self.__list[indicies[choice]]
