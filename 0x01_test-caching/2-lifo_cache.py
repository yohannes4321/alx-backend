from collections import OrderedDict
from base_caching import BaseCaching
class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data=OrderedDict()
    def put(self,key,item):
        self.cache_data[key]=item
        if len(self.cache_data)> self.MAX_ITEMS:
            order_index,order_item=self.cache_data.popitem(last=True)
            print("DISCARD {}".format(order_index))
    def get(self,key):
        if self.cache_data.keys() is None or self.cache_data.get(key) is None:
            return None 
        
        return self.cache_data[key]
