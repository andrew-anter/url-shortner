from functions import url_shortner


def test_url_shortner():
    test_url1 = "www.google.com"

    shortned_url1 = url_shortner(url=test_url1)
    shortned_url2 = url_shortner(url=test_url1)

    assert shortned_url1 == shortned_url2
