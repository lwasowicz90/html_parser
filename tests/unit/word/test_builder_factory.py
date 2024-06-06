import pytest
from unittest.mock import patch, MagicMock

import word.builder_factory as uut


@patch('word.builder_factory.IWordBuilder')
@patch('word.builder_factory.is_valid_ascii')
def test_create_english_word_builder(is_valid_ascii_mock: MagicMock, word_builder_class_mock: MagicMock):
    test_policy = uut.WordBuilderPolicy.ENGLISH_WORD_POLICY

    result = uut.create(test_policy)

    assert result == word_builder_class_mock.return_value
    word_builder_class_mock.assert_called_once_with(is_valid_ascii_mock)


@patch('word.builder_factory.IWordBuilder')
@patch('word.builder_factory.is_valid_unicode')
def test_create_latin_word_builder(is_valid_unicode_mock: MagicMock, word_builder_class_mock: MagicMock):
    test_policy = uut.WordBuilderPolicy.LATIN_LANGUAGE_POLICY

    result = uut.create(test_policy)

    assert result == word_builder_class_mock.return_value
    word_builder_class_mock.assert_called_once_with(is_valid_unicode_mock)


def test_incorrect_policy():
    test_policy = 'dummy'

    with pytest.raises(Exception) as ex_info:
        uut.create(test_policy)

    assert isinstance(ex_info.value, ValueError)
