"""Implement Trie data structure."""

class Trie(object):
    """Trie data structure."""
    def __init__(self):
        self.words = {}

    def contains(self, s):
        """Test that string s is contained within the trie."""
        words = self.words
        for c in s:
            if c not in words:
                return False
            words = words[c]
        return words.get('$', False)

    def insert(self, s):
        words = self.words
        for c in s:
            words = words.setdefault(c, {})
        words['$'] = True
