import pytest
from functions import (
    url_shortner_md5,
    url_shortner_alphanumeric,
    URL_LEN,
    url_shortner_by_base_conversion,
)


@pytest.fixture
def test_url() -> str:
    return "www.google.com"


def test_url_shortner_md5(test_url: str):
    shortned_url1 = url_shortner_md5(url=test_url)
    shortned_url2 = url_shortner_md5(url=test_url)

    assert shortned_url1 == shortned_url2

    short_url_code = shortned_url1.rsplit("/", 1)[-1]
    assert len(short_url_code) == URL_LEN


def test_url_shortner_alphanumeric(test_url: str):
    shortned_url1 = url_shortner_alphanumeric(url=test_url)
    shortned_url2 = url_shortner_alphanumeric(url=test_url)

    assert shortned_url1 == shortned_url2

    short_url_code = shortned_url1.rsplit("/", 1)[-1]
    assert len(short_url_code) == URL_LEN


def test_url_shortner_by_base_conversion(test_url: str):
    shortned_url1 = url_shortner_by_base_conversion(url=test_url)
    shortned_url2 = url_shortner_by_base_conversion(url=test_url)

    assert shortned_url1 == shortned_url2
