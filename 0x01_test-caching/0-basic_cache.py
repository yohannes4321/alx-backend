from base_caching import BaseCaching
from collections import OrderedDict
class BasicCache (BaseCaching):
    def __init__(self):
        """ intialize the basic cache from the parent class so 
        use it all the function and constants from the parrent class
        and use them as self."""
        super().__init__()
        self.cache_data=OrderedDict()
    def put(self,key,item):
        self.cache_data[key]=item
        if len(self.cache_data) > self.MAX_ITEMS:
            oldest_key,oldest_item=self.cache_data.popitem(last=False)
            # i have put last false because i want to delete the the first element 
            print("DISCARD {}".format(oldest_key))
    def get(self,key):
        if self.cache_data.keys()is None or self.cache_data.get(key) is None:
            return None 
        return self.cache_data[key]