from base_caching import BaseCaching

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.lru_order = []  # Contains the order of keys based on usage

    def put(self, key, item):
        if key is None or item is None:
            return 

        # If key is already in cache, update its position in LRU order
        if key in self.cache_data:
            self.lru_order.remove(key)

        # If cache exceeds MAX_ITEMS, remove the least recently used item
        if len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = self.lru_order.pop(0)  # Remove the oldest entry from order list
            del self.cache_data[oldest_key]  # Remove from cache

        # Insert the item in cache and update LRU order
        self.cache_data[key] = item
        self.lru_order.append(key)  # Mark this key as the most recently used

    def get(self,key):
        if key is None or not self.cache_data.get(key):
            return 
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data
