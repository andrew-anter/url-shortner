from functions import url_shortner


def test_nothing():
    assert True


def test_url_shortner():
    test_url1 = "www.google.com"
    test_url2 = "www.google.com"

    shortned_url1 = url_shortner(url=test_url1)
    shortned_url2 = url_shortner(url=test_url2)

    assert shortned_url1 == shortned_url2
