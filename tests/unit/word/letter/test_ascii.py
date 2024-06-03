import pytest

import word.letter.ascii as uut

@pytest.mark.parametrize(
        'test_char_num, expected',
        [(1, False),
         (64, False),
         (65, True),
         (89, True),
         (90, True),
         (91, False),
         (98, False)])
def test_is_upper_letter(test_char_num: int, expected: bool):
    assert uut.is_upper_letter(test_char_num) is expected


@pytest.mark.parametrize(
        'test_char_num, expected',
        [(1, False),
         (64, False),
         (65, False),
         (89, False),
         (90, False),
         (96, False),
         (97, True),
         (98, True),
         (122, True),
         (123, False)])
def test_is_lower_letter(test_char_num: int, expected: bool):
    assert uut.is_lower_letter(test_char_num) is expected


@pytest.mark.parametrize('test_text',
                         [
                            'ss', 'test', 'some data'
                         ])
def test_is_valid_raises_on_invalid_length(test_text: str):
    with pytest.raises(Exception) as ex_info:
        uut.is_valid(test_text)
    
    assert isinstance(ex_info.value, ValueError)


@pytest.mark.parametrize('test_text',
                         [
                            'a', 'b', 'k', 'z', 'y', 'A', 'B', 'K', 'Z', 'Y', "'"
                         ],
                         ids=['lower_case_a', 'lower_case_b', 'lower_case_k', 'lower_case_z', 'lower_case_y',
                              'upper_case_a', 'upper_case_b', 'upper_case_k', 'upper_case_z', 'upper_case_y',
                              'apostrophe'])
def test_is_valid(test_text: str):
    assert uut.is_valid(test_text) is True


@pytest.mark.parametrize('test_text',
                         list("""1234567890-=!@#$%^&*()_+`~,.<>/?";:]}[]}{"""))
def test_is_valid_invalid_char(test_text: str):
    assert uut.is_valid(test_text) is False
