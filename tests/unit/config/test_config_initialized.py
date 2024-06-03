from config import CONFIG, Settings


def test_config_initialized():
    assert CONFIG
    assert isinstance(CONFIG, Settings)
