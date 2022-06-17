from pkg_resources import get_distribution

__version__ = get_distribution("boilerplate").version


def test_version():
    assert __version__ == "0.1.0"
