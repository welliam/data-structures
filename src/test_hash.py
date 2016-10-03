import pytest

VALUES = ['', 'asd', 'hello world', '65sdf679adgdugcoungysd529g3r7c4']
WORDS = '/usr/share/dict/words'


@pytest.fixture
def table():
    """A simple hash table using additive hashing."""
    from hash_table import HashTable, additive_hash
    return HashTable(1024, additive_hash)


@pytest.fixture
def rotating_table():
    """A simple hash table using additive hashing."""
    from hash_table import HashTable, rot_hash
    return HashTable(1024, rot_hash)


@pytest.fixture
def oat_table():
    """A simple hash table using one at a time hashing."""
    from hash_table import HashTable, oat_hash
    return HashTable(1024, oat_hash)


@pytest.fixture
def fnv_table():
    """A simple hash table using FNV hashing."""
    from hash_table import HashTable, fnv_hash
    return HashTable(1024, fnv_hash)


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


@pytest.mark.parametrize('value', VALUES)
def test_set_and_get_rot(value, rotating_table):
    """Test setting a value in a table and retrieving it."""
    rotating_table.set(value, value)
    assert rotating_table.get(value) == value


def test_against_dict_rot(rotating_table):
    """Test creating a dictionary of word in WORDS."""
    for word in open(WORDS):
        rotating_table.set(word, word)
    for word in open(WORDS):
        assert rotating_table.get(word) == word


@pytest.mark.parametrize('value', VALUES)
def test_set_and_get_oat(value, oat_table):
    """Test setting a value in a table and retrieving it."""
    oat_table.set(value, value)
    assert oat_table.get(value) == value


def test_against_dict_oat(oat_table):
    """Test creating a dictionary of word in WORDS."""
    for word in open(WORDS):
        oat_table.set(word, word)
    for word in open(WORDS):
        assert oat_table.get(word) == word


@pytest.mark.parametrize('value', VALUES)
def test_set_and_get_fnv(value, fnv_table):
    """Test setting a value in a table and retrieving it."""
    fnv_table.set(value, value)
    assert fnv_table.get(value) == value


def test_against_dict_fnv(fnv_table):
    """Test creating a dictionary of word in WORDS."""
    for word in open(WORDS):
        fnv_table.set(word, word)
    for word in open(WORDS):
        assert fnv_table.get(word) == word


def test_get_raises_key_error(table):
    """Test getting a key not in the table raises KeyError."""
    with pytest.raises(KeyError):
        table.get('hello')


# These tests always fail. We calculate the bucket with the largest
# number of collisions, then test that that value is less than or
# equal to the number of words in the table divided by the number of
# buckets (i.e., if the hash function is perfect).

# from hash_table import fnv_hash, oat_hash, additive_hash, rot_hash
# HASH_FUNCTIONS = [fnv_hash, oat_hash, additive_hash, rot_hash]
# @pytest.mark.parametrize('hash_function', HASH_FUNCTIONS)
# def test_stress(hash_function):
#     from hash_table import HashTable
#     table = HashTable(1024, hash_function)
#     num_words = 0
#     for word in open(WORDS):
#         table.set(word, word)
#         num_words += 1
#     num_buckets = len(table._buckets)
#     worst_ratio = max(map(len, table._buckets))
#     assert worst_ratio <= num_words // num_buckets
