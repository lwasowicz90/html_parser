import pytest
from unittest.mock import MagicMock

import word.builder as word_builder


def test_list_of_abstract_word_builder_methods():
    uut = word_builder.AbstractWordBuilder
    a_methods = list(filter(lambda name: name[0] != '_', dir(uut)))
    
    assert len(a_methods) == 3    
    assert 'append_char' in a_methods
    assert 'build' in a_methods
    assert 'empty' in a_methods


def test_word_empty_when_builder_initialized():
    uut  = word_builder.IWordBuilder(MagicMock())
    
    assert uut.empty is True


def test_append_char_then_not_empty():
    mock_validator = MagicMock(return_value = True)
    uut = word_builder.IWordBuilder(mock_validator)
    assert uut.empty is True
    uut.append_char('X')
    
    result = uut.empty

    assert result is False    


def test_append_chars_then_build():
    mock_validator = MagicMock(side_effect = [True, True, True, True])
    uut = word_builder.IWordBuilder(mock_validator)
    assert uut.empty is True
    uut.append_char('c')
    uut.append_char('o')
    uut.append_char('d')
    uut.append_char('e')
    
    result = uut.build()

    assert result == 'code'


def test_append_chars_then_build_when_some_letters_ignored():
    mock_validator = MagicMock(side_effect = [True, False, False, True])
    uut = word_builder.IWordBuilder(mock_validator)
    assert uut.empty is True

    uut.append_char('c')
    uut.append_char('o')
    uut.append_char('d')
    uut.append_char('e')

    result = uut.build()

    assert result == 'ce'


def test_append_char_raises_after_build():
    mock_validator = MagicMock(side_effect = [True, True, True, True])
    uut = word_builder.IWordBuilder(mock_validator)
    assert uut.empty is True
    uut.append_char('c')
    uut.append_char('o')
    uut.append_char('d')
    uut.build()

    with pytest.raises(Exception) as ex_info:
        uut.append_char('e')
    
    assert isinstance(ex_info.value, OverflowError)


def test_build_more_than_once_raises():
    mock_validator = MagicMock(side_effect = [True, True, True, True])
    uut = word_builder.IWordBuilder(mock_validator)
    assert uut.empty is True
    uut.append_char('c')
    uut.build()

    with pytest.raises(Exception) as ex_info:
        uut.build()

    assert isinstance(ex_info.value, RuntimeError)
