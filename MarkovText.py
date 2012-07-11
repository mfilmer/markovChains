import random

class markov(object):
    def __init__(self):
        self.__fileName = ''
        self.__wordCount = 0
        self.__words = []
    
    def seedFile(self,fileName):
        self.__wordCount = 0
        with open(fileName) as f:
            self.__words = f.read().split()
            self.__wordCount = len(self.__words)
        if self.__wordCount == 0:
            error('seed file not loaded or is empty')
    
    def seedString(self,words):
        self.__wordCount = 0
        self.__words = words.split()
        self.__wordCount = len(self.__words)
    
    def seedList(self,items):
        self.__wordCount = 0
        self.__words = items
        self.__wordCount = len(self.__words)
    
    def genText(self,length,seedWords=2):
        if self.__wordCount == 0:
            error('seed file not loaded or seed file is empty')
        if self.__wordCount < seedWords:
            error('too few words in seed file')
        SWI = random.randint(0,self.__wordCount - (seedWords+1))
        
        seed = self.__words[SWI:SWI+seedWords]
        return self.genTextFromSeed(length,seed)
    
    def genTextFromSeed(self,length,seed):
        #do this so we don't modify the original seed
        words = seed
        for i in range(length-len(words)):
            seed.append(self.__getNextWord(words[i:]))
        return words
    
    def __getNextWord(self,words):
        indicies = []
        num = len(words)
        stop = self.__wordCount
        for i in range(num,stop):
            if self.__words[i-num:i] == words:
                indicies.append(i)
        count = len(indicies)
        if count == 0:
            return ''
        choice = random.randint(0,count-1)
        return self.__words[indicies[choice]]
