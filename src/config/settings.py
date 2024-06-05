"""Defines config fields and load it from file
"""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class responsible to define config fields
    """
    log_to_file: bool = Field(default=True, frozen=True)
    log_to_stdout: bool = Field(default=False, frozen=True)
    log_level: str = Field(default="DEBUG", frozen=True)
    html_entity_name_separators: list[str] = Field(description='Entity name that is treated as word separator',
                                                   frozen=True)
    tags_ignored: set[str] = Field(description='Tags name to ignore to process', frozen=True)
    url: str = Field(description='Web page url to process', frozen=True)
    model_config = SettingsConfigDict(env_file="src/config.env")
