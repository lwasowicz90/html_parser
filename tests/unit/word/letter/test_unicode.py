# -*- coding: utf-8 -*-
import pytest

import word.letter.unicode as uut

@pytest.mark.parametrize(
        'test_char_num, expected',
        [(ord('a'), False),
         (ord('A'), False),
         (ord('z'), False),
         (ord('Z'), False),
         (ord('1'), False),
         (ord('9'), False),
         (ord('×'), False),
         (ord('À'), True),
         (ord('Ë'), True),
         (ord('Õ'), True),
         (ord('Ø'), True),
         (ord('Ý'), True),         
         (ord('Þ'), True),
         (ord('ß'), False),
         (ord('ö'), False)])
def test_is_upper_latin1_sup_letter(test_char_num: int, expected: bool):
    assert uut.is_upper_latin1_sup_letter(test_char_num) is expected


@pytest.mark.parametrize(
        'test_char_num, expected',
        [(ord('a'), False),
         (ord('A'), False),
         (ord('z'), False),
         (ord('Z'), False),
         (ord('1'), False),
         (ord('9'), False),
         (ord('×'), False),
         (ord('À'), False),
         (ord('Ý'), False),
         (ord('÷'), False),         
         (ord('ß'), True),
         (ord('ã'), True),
         (ord('õ'), True),
         (ord('ø'), True),
         (ord('ü'), True),
         ])
def test_is_upper_latin1_sup_letter(test_char_num: int, expected: bool):
    assert uut.is_lower_latin1_sup_letter(test_char_num) is expected


@pytest.mark.parametrize(
        'test_char_num, expected',
        [(ord('a'), False),
         (ord('A'), False),
         (ord('z'), False),
         (ord('Z'), False),
         (ord('1'), False),
         (ord('9'), False),
         (ord('À'), False),
         (ord('ü'), False),
         (ord('Ā'), True),
         (ord('Č'), True),
         (ord('ģ'), True),
         (ord('Ľ'), True),
         (ord('Ś'), True),
         (ord('Ž'), True),
         (ord('ŵ'), True),
         ])
def test_is_eu_latin_extended_a_letter(test_char_num: int, expected: bool):
    assert uut.is_eu_latin_extended_a_letter(test_char_num) is expected


@pytest.mark.parametrize(
        'test_char_num, expected',
        [(ord('a'), False),
         (ord('A'), False),
         (ord('z'), False),
         (ord('Z'), False),
         (ord('1'), False),
         (ord('9'), False),
         (ord('À'), False),
         (ord('ü'), False),
         (ord('Ā'), False),
         (ord('Ľ'), False),
         (ord('ŵ'), False),
         (ord('ƀ'), True),
         (ord('Ɠ'), True),
         (ord('Ț'), True),
         (ord('ǻ'), True),
         (ord('Ȱ'), True),
         ])
def test_is_latin_extended_b_letter(test_char_num: int, expected: bool):
    assert uut.is_latin_extended_b_letter(test_char_num) is expected


@pytest.mark.parametrize('test_char',
                         [
                            'a', 'A', 'b', 'B', 'À', 'Ü', 'ã', 'ö', 'ú', 'Ą', 'ĉ', 'Ę', 'Ĥ', 'Ň', 'Ž', 'Ƌ', 'Ƙ', 'ƿ',
                            'Ǚ', 'Ǹ', 'Ȯ'
                         ],
                         )
def test_is_valid(test_char: str):
    assert uut.is_valid(test_char) is True


@pytest.mark.parametrize('test_text',
                          list("""1234567890-=!@#$%^&*()_+`~,.<>/?";:]}[]}{"""))
def test_is_valid_invalid_char(test_text: str):
    assert uut.is_valid(test_text) is False
