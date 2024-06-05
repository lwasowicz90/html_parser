import pytest

from typing import NamedTuple, Any

from config import Settings


class ExpectedFieldProps(NamedTuple):
    field_name: str    
    type: str
    default: Any | None = None
    description: str | None = None
    items_type: str | None = None
    items_unique: bool | None = None


SETTINGS_TEST_PARAMS = [
    ExpectedFieldProps(field_name='log_to_file', type='boolean', default=True,),
    ExpectedFieldProps(field_name='log_to_stdout', type='boolean', default=False),
    ExpectedFieldProps(field_name='log_level', type='string', default='DEBUG'),
    ExpectedFieldProps(field_name='html_entity_name_separators', type='array', description='Entity name that is treated as word separator', items_type='string'),
    ExpectedFieldProps(field_name='tags_ignored', type='array', description='Tags name to ignore to process', items_type='string', items_unique=True),
    ExpectedFieldProps(field_name='url', type='string', description='Web page url to process'),
]


@pytest.mark.parametrize('expected_field_props',
                         SETTINGS_TEST_PARAMS)
def test_settings_fields(expected_field_props: ExpectedFieldProps):
    field_props = Settings.model_json_schema()['properties'][expected_field_props.field_name]

    assert field_props['type'] == expected_field_props.type
    assert field_props.get('default') == expected_field_props.default
    assert field_props.get('description') == expected_field_props.description
    assert field_props.get('items', {}).get('type') == expected_field_props.items_type
    assert field_props.get('uniqueItems') == expected_field_props.items_unique


def test_settings_fields_number():
    assert len(Settings.model_json_schema()['properties']) == len(SETTINGS_TEST_PARAMS)
