from functions import url_shortner_md5, url_shortner_alphanumeric


def test_url_shortner_md5():
    test_url1 = "www.google.com"

    shortned_url1 = url_shortner_md5(url=test_url1)
    shortned_url2 = url_shortner_md5(url=test_url1)

    assert shortned_url1 == shortned_url2


def test_url_shortner_alphanumeric():
    test_url1 = "www.google.com"

    shortned_url1 = url_shortner_alphanumeric(url=test_url1)
    shortned_url2 = url_shortner_alphanumeric(url=test_url1)

    assert shortned_url1 == shortned_url2
