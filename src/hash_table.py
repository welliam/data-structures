def additive_hash(s):
    """Really bad hash function.

    Like, terrible."""
    return sum(map(ord, s))


def fnv_hash(s):
    """Fowler/Noll/Vo hashing."""
    h = 2166136261
    for c in s:
        h = (h * 16777619) ^ ord(c)
    return h


def rot_hash(s):
    """Rotating hash function."""
    res = 0
    for c in s:
        res = (res << 4) ^ (res >> 28) ^ ord(c)
    return res


def oat_hash(s):
    """One at a time hashing."""
    h = 0
    for c in s:
        h += ord(c)
        h += h << 10
        h ^= h >> 6
    h += h << 3
    h ^= h >> 11
    h += h << 15
    return h


class HashTable(object):
    """A hash table."""

    def __init__(self, capacity, hash_function):
        """Initialize buckets and store the hash function."""
        self._buckets = []
        for _ in range(capacity):
            self._buckets.append([])
        self._hash = hash_function

    def _get_bucket(self, k):
        """Get the right bucket for the input."""
        return self._buckets[self._hash(k) % len(self._buckets)]

    def get(self, key):
        """Get the value associated with key in the table."""
        for k, v in self._get_bucket(key):
            if k == key:
                return v
        raise KeyError('Key not in table.')

    def set(self, key, value):
        """Set the value associated with key in the table to value."""
        bucket = self._get_bucket(key)
        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = key, value
                return
        bucket.append((key, value))
