from base_caching import BaseCaching
from collections import OrderedDict
class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.freq={}
        self.key=[]
        self.cache_data=OrderedDict()

    def put(self, key, item):
        if key is None or item is None:
            return
        
        self.cache_data[key]=item
        if key not in self.freq:
            self.freq[key]=1
        else:
            self.freq[key]+=1
        if self.freq[key]==0:
            del self.freq[key]
        if len(self.cache_data)>self.MAX_ITEMS:
            # return smallles frequency key
            key.append(min(self.freq[key]))


        

    def get(self, key):
      
