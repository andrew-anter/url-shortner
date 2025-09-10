import hashlib
import random
import string

url_dict = {}
URL_LEN = 8
BASE_DOMAIN = "localhost"
PROTOCOL = "http"
BASE_URL = f"{PROTOCOL}://{BASE_DOMAIN}"


def url_shortner_md5(*, url: str) -> str:
    """
    Supports 16 ^ URL_LEN
    in case of URL_LEN = 8 then it will support approximately 4B
    """
    url_utf8_encoded = url.encode("utf-8")
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(url_utf8_encoded)

    ## will work for 4B urls
    shortened_url_code = md5_hash_object.hexdigest()[:URL_LEN]

    if shortened_url_code not in url_dict:
        url_dict[shortened_url_code] = url_utf8_encoded

    return f"{BASE_URL}/{shortened_url_code}"


def url_shortner_alphanumeric(*, url: str) -> str:
    """
    Supports 62 ^ URL_LEN
    in case of URL_LEN = 8 then it will support approximately 2*10 ^ 14
    """
    characters: list[str] = [character for character in string.ascii_letters] + [
        str(number) for number in range(0, 10)
    ]
    url_utf8_encoded = url.encode("utf-8")

    shortened_url_code = ""

    if url_utf8_encoded in url_dict:
        shortened_url_code = url_dict[url_utf8_encoded]
    else:
        shortened_url_code = "".join(random.choice(characters) for _ in range(URL_LEN))
        url_dict[url_utf8_encoded] = shortened_url_code

    return f"{BASE_URL}/{shortened_url_code}"
