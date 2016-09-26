"""Implement Trie data structure."""


class Trie(object):
    """Trie data structure."""
    def __init__(self):
        self.words = {}

    def contains(self, s):
        """Return whether a string is contained within the trie."""
        words = self.words
        for c in s:
            if c == '$' or c not in words:
                return False
            words = words[c]
        return words.get('$', False)

    def insert(self, s):
        """Insert string into trie."""
        words = self.words
        if '$' in s:
            raise ValueError('String inserted into trie must not contain $.')
        for c in s:
            words = words.setdefault(c, {})
        words['$'] = True

    def traverse(self, start):
        """Traverse the trie from start."""
        start = self.words
        stack = [start]
        word = []
        while len(stack):
            curr = stack.pop()
            for key in curr:
                if key != '$':
                    stack.append(curr[key])
                    word.append(key)
                else:
                    print(word)
