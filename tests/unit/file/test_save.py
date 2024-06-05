from unittest.mock import patch, mock_open

from file.save import save_to_file


@patch("builtins.open", new_callable=mock_open)
@patch("file.save.json.dump")
def test_save_to_file(json_dump_mock, open_mock):
    test_data = {'a': 2, 'c': 1}
    
    save_to_file(test_data)

    open_mock.assert_called_with('result.txt', 'w', encoding='utf-8')
    json_dump_mock.assert_called_with(test_data, open_mock.return_value, indent=2)


@patch("builtins.open", new_callable=mock_open)
@patch("file.save.json.dump")
def test_save_to_file_custom_filename(json_dump_mock, open_mock):
    test_data = {'a': 2, 'c': 1}
    custom_filename = 'dummy.txt'
    
    save_to_file(test_data, custom_filename)

    open_mock.assert_called_with(custom_filename, 'w', encoding='utf-8')
    json_dump_mock.assert_called_with(test_data, open_mock.return_value, indent=2)
