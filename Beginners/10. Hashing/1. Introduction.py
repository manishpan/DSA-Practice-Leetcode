names = ['alice', 'brad', 'collin', 'brad', 'dylan', 'kim']

CountMap = {}

for name in names:
    #If name not in CountMap
    if name not in CountMap:
        CountMap[name] = 1
    else:
        CountMap[name] += 1

print(CountMap)

#Implementating simple hashMap

class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)         #Calculating sum, this can vary
        return index % self.capacity #Hash function
    
    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None
    
    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val == val
                return 
            
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity  #We should find next prime numbers but its an easy implementation
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)
        
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)