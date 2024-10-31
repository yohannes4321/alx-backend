from base_caching import BaseCaching

class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.mru_order = []  # Keeps track of the most recently used keys

    def put(self, key, item):
        if key is None or item is None:
            return

        # If key exists, remove it to update its position later
        if key in self.cache_data:
            self.mru_order.remove(key)

        # If cache exceeds MAX_ITEMS, remove the most recently used item
        if len(self.cache_data) >= self.MAX_ITEMS:
            most_recent_key = self.mru_order.pop()  # Remove the most recent entry
            del self.cache_data[most_recent_key]

        # Add item to cache and mark it as the most recently used
        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Update MRU order, moving the accessed key to the end
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
