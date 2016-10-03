import pytest

VALUES = ['', 'asd', 'hello world', '65sdf679adgdugcoungysd529g3r7c4']
WORDS = '/usr/share/dict/words'


@pytest.fixture
def table():
    """A simple hash table using additive hashing."""
    from hash_table import HashTable, additive_hash
    return HashTable(1024, additive_hash)


@pytest.mark.parametrize('value', VALUES)
def test_set_and_get(value, table):
    """Test setting a value in a table and retrieving it."""
    table.set(value, value)
    assert table.get(value) == value


def test_against_dict(table):
    """Test creating a dictionary of word in WORDS."""
    for word in open(WORDS):
        table.set(word, word)
    for word in open(WORDS):
        assert table.get(word) == word
