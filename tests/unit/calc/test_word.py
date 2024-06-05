import pytest
from unittest.mock import patch, MagicMock

from calc.word import get_occurences, get_top_n_occurences

@pytest.fixture
def words():
    return ['test', 'test', 'test' , 'data', 'data', 'd', 'a']


@patch('calc.word.Counter')
def test_get_occurences(counter_mock: MagicMock, words):
    result = get_occurences(words)

    assert result == counter_mock.return_value
    counter_mock.assert_called_once_with(words)


def test_get_occurences_no_mock(words):
    result = get_occurences(words)

    assert result == {'test': 3, 'data': 2, 'd': 1, 'a': 1}


def test_get_top_n_occurences():
    n = 5
    words = (*['first']*10, *['second']*5, *['thirth']*4, *['fourth']*4, *['fifth']*3, *['sixth']*2, 'seventh')
    print(words)

    result = get_top_n_occurences(words, n)

    assert result == {'first': 10, 'second': 5, 'thirth': 4, 'fourth': 4, 'fifth': 3}
