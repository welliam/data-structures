"""Test trie.py."""

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


def test_trie_insert_dollar():
    """Test trie will reject inserting a string containing $."""
    from .trie import Trie
    with pytest.raises(ValueError):
        Trie().insert('$')


def test_trie_contains_dollar():
    """Test trie will reject looking up string with $."""
    from .trie import Trie
    t = Trie()
    t.insert('a')
    assert not t.contains('a$ uh oh!')


def comesbefore(t, a, b):
    """Used in testing traversal methods."""
    return b in t[t.index(a):]


def test_traversal_empty():
    """Test traversal of an empty tree returns []."""
    from .trie import Trie
    assert list(Trie().traverse()) == []


def test_traversal_basic():
    """Test traversal of a tree with an empty word."""
    from .trie import Trie
    t = Trie()
    t.insert('')
    assert list(t.traverse()) == ['']


def test_traversal_word():
    """Test traversal of a tree with a single-char word."""
    from .trie import Trie
    t = Trie()
    t.insert('a')
    assert list(t.traverse()) == ['a']


def test_traversal_word_deep():
    """Test traversal of a tree with a multi-char word."""
    from .trie import Trie
    t = Trie()
    t.insert('aa')
    assert list(t.traverse()) == ['aa']


def test_traversal_word_deep_start():
    """Test traversal of a tree with a multi-char word and start word."""
    from .trie import Trie
    t = Trie()
    t.insert('a')
    t.insert('aa')
    assert list(t.traverse()) == ['a', 'aa']


def test_traversal_word_deep_bad_start():
    """Test traversal of a tree with a multi-char word and bad start word."""
    from .trie import Trie
    t = Trie()
    t.insert('aa')
    with pytest.raises(KeyError):
        list(t.traverse('b'))


def test_starting():
    """Test auto complete working correctly."""
    from .trie import Trie
    t = Trie()
    t.insert('a')
    t.insert('ab')
    t.insert('ba')
    results = ['a', 'ab']
    for item in list(t.traverse('a')):
        assert item in results


def test_traversal_word_deep_2():
    """Test traversal of a tree with a multi-char word."""
    from .trie import Trie
    t = Trie()
    t.insert('aaaaa')
    assert list(t.traverse()) == ['aaaaa']


def test_traversal_word_order():
    """Test traversal of a tree is depth-first."""
    from .trie import Trie
    t = Trie()
    t.insert('a')
    t.insert('aa')
    t.insert('b')
    t.insert('bb')
    result = list(t.traverse())

    # because which branch we visit first is random, we have to figure
    # out which branch we traversed first to determine if the search
    # was depth-first
    if comesbefore(result, 'a', 'b'):
        assert comesbefore(result, 'aa', 'b')
    else:
        assert comesbefore(result, 'bb', 'a')
