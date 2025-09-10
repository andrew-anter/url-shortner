from functions import url_shortner_md5, url_shortner_alphanumeric, URL_LEN


def test_url_shortner_md5():
    test_url1 = "www.google.com"

    shortned_url1 = url_shortner_md5(url=test_url1)
    shortned_url2 = url_shortner_md5(url=test_url1)

    assert shortned_url1 == shortned_url2

    short_url_code = shortned_url1.rsplit("/", 1)[-1]
    assert len(short_url_code) == URL_LEN


def test_url_shortner_alphanumeric():
    test_url1 = "www.google.com"

    shortned_url1 = url_shortner_alphanumeric(url=test_url1)
    shortned_url2 = url_shortner_alphanumeric(url=test_url1)

    assert shortned_url1 == shortned_url2

    short_url_code = shortned_url1.rsplit("/", 1)[-1]
    assert len(short_url_code) == URL_LEN
