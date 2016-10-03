def additive_hash(s):
    """Really bad hash function.

    Like, terrible."""
    return sum(map(ord, s))


class HashTable(object):
    """A hash table."""
    def __init__(self, capacity, hash_function):
        self._buckets = []
        for _ in range(capacity):
            self._buckets.append([])
        self._hash = hash_function

    def _get_bucket(self, k):
        return self._buckets[self._hash(k) % len(self._buckets)]

    def get(self, key):
        for k, v in self._get_bucket(key):
            if k == key:
                return v

    def set(self, key, value):
        bucket = self._get_bucket(key)
        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = key, value
                return
        bucket.append((key, value))
