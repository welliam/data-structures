"Test trie.py."""

import pytest


INSERT_STRINGS = ['hi', 'test', '', 'foo bar']

NONEMPTY_STRINGS = ['hello', 'hi', 'h', 'foobar', 'quux']

WORDS = [
    "artsier",
    "artsiest",
    "artsy",
    "artwork",
    "artwork's",
    "artworks",
    "arty",
    "as",
    "asbestos",
    "asbestos's",
    "ascend",
    "ascendancy",
    "ascendancy's",
    "ascendant",
    "ascendant's",
    "ascendants",
    "ascended",
    "ascendency",
    "ascendency's",
    "ascendent",
    "ascendent's",
    "ascendents",
    "ascending",
    "ascends",
    "ascension",
    "ascension's",
    "ascensions",
    "ascent",
    "ascent's",
    "ascents",
    "ascertain",
    "ascertainable",
    "ascertained",
    "ascertaining",
    "ascertains",
    "ascetic",
    "ascetic's",
    "asceticism"
]


def test_empty_trie():
    """Test empty trie contains nothing."""
    from .trie import Trie
    assert not Trie().contains('hi')


@pytest.mark.parametrize('s', INSERT_STRINGS)
def test_trie_insert(s):
    """Test trie contains inserted string."""
    from .trie import Trie
    t = Trie()
    t.insert(s)
    assert t.contains(s)


@pytest.mark.parametrize('s', NONEMPTY_STRINGS)
def test_trie_false_on_truncations(s):
    """Test trie contains inserted string."""
    from .trie import Trie
    t = Trie()
    t.insert(s)
    assert not t.contains(s[:-1])


def test_trie_many_words():
    """Test trie containing many words."""
    from .trie import Trie
    t = Trie()
    for word in WORDS:
        t.insert(word)
    for word in WORDS:
        assert t.contains(word)
