from base_caching import BaseCaching
from collections import OrderedDict
class FIFOCache(BaseCaching):
    def __init__(self):
  
        
        super().__init__()
        # to inherit from the parrent class i use super().__init__
        self.cache_data=OrderedDict()
    def put(self,key,item):
        self.cache_data[key]=item
        if len(self.cache_data)> self.MAX_ITEMS:
            order_key,order_items=self.cache_data.popitem(last=False)
            print("DISCARD {}".format(order_key))
    def get(self,key):
        if self.cache_data.key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]


