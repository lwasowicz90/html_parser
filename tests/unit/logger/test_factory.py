import pytest
from freezegun import freeze_time
from unittest.mock import patch, MagicMock, call

import logging

import logger.factory as uut



@pytest.fixture
def expected_log_format():
    return '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


@patch('logger.factory.CONFIG', MagicMock(**{'log_to_stdout': True, 'log_to_file': True, 'log_level': 'INFO'}))
@patch('logger.factory.create_stream_handler', MagicMock())
@patch('logger.factory.create_file_handler', MagicMock())
@patch('logger.factory.logging.getLogger')
def test_init_logger_with_handlers(get_logger_mock: MagicMock):
    root_logger_mock = MagicMock()
    get_logger_mock.return_value = root_logger_mock

    uut.init()

    get_logger_mock.assert_called_once_with('root')
    expected_level = logging.INFO
    root_logger_mock.setLevel.assert_called_once_with(expected_level)
    root_logger_mock.addHandler.assert_has_calls([call(uut.create_stream_handler.return_value),
                                                  call(uut.create_file_handler.return_value)])
    uut.create_stream_handler.assert_called_once_with(expected_level)
    uut.create_file_handler.assert_called_once_with(expected_level)


@patch('logger.factory.CONFIG', MagicMock(**{'log_to_stdout': False, 'log_to_file': False, 'log_level': 'INFO'}))
@patch('logger.factory.create_stream_handler', MagicMock())
@patch('logger.factory.create_file_handler', MagicMock())
@patch('logger.factory.logging.getLogger')
def test_init_logger_with_no_handlers(get_logger_mock: MagicMock):
    root_logger_mock = MagicMock()
    get_logger_mock.return_value = root_logger_mock

    uut.init()

    get_logger_mock.assert_called_once_with('root')
    expected_level = logging.INFO
    root_logger_mock.setLevel.assert_called_once_with(expected_level)
    root_logger_mock.addHandler.assert_not_called()
    uut.create_stream_handler.assert_not_called()
    uut.create_file_handler.assert_not_called()


@patch('logger.factory.CONFIG', MagicMock(**{'log_to_stdout': False, 'log_to_file': False, 'log_level': 'DUMMY'}))
@patch('logger.factory.logging.getLogger')
def test_init_logger_with_incorrect_log_level_in_config(get_logger_mock: MagicMock):
    root_logger_mock = MagicMock()
    get_logger_mock.return_value = root_logger_mock

    uut.init()

    get_logger_mock.assert_called_once_with('root')
    expected_level = logging.DEBUG
    root_logger_mock.setLevel.assert_called_once_with(expected_level)



@patch('logger.factory.logging.Formatter')
@patch('logger.factory.logging.StreamHandler')
def test_create_stream_handler(stream_handler_mock: MagicMock,
                               formatter_mock: MagicMock,                               
                               expected_log_format):
    dummy_level = 10

    result = uut.create_stream_handler(dummy_level)

    assert result == stream_handler_mock.return_value
    stream_handler_mock.assert_called_once()
    stream_handler_mock.return_value.setLevel.assert_called_once_with(dummy_level)
    stream_handler_mock.return_value.setFormatter.assert_called_once_with(formatter_mock.return_value)
    formatter_mock.assert_called_once_with(expected_log_format)


TEST_FILENAME = 'dummy_filename'


@patch('logger.factory.get_filename', MagicMock(return_value=TEST_FILENAME))
@patch('logger.factory.logging.Formatter')
@patch('logger.factory.logging.FileHandler')
def test_create_file_handler(file_handler_mock: MagicMock,
                             formatter_mock: MagicMock,
                             expected_log_format):
    dummy_level = 10

    result = uut.create_file_handler(dummy_level)

    assert result == file_handler_mock.return_value
    file_handler_mock.assert_called_once_with(TEST_FILENAME)
    file_handler_mock.return_value.setLevel.assert_called_once_with(dummy_level)
    file_handler_mock.return_value.setFormatter.assert_called_once_with(formatter_mock.return_value)
    formatter_mock.assert_called_once_with(expected_log_format)


FREEZED_DT = '2024-05-11 20:56:11.234'


@freeze_time(FREEZED_DT)
def test_get_filename():
    assert uut.get_filename() == 'log_11_05_2024_20_56_11.txt'
