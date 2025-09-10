import hashlib
import random
import string

url_dict = {}
base_domain = "localhost"
protocol = "http"
base_url = f"{protocol}://{base_domain}"


def url_shortner_md5(*, url: str) -> str:
    """
    supports to 16^8 => 4B.
    """
    url_utf8_encoded = url.encode("utf-8")
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(url_utf8_encoded)

    ## will work for 4B urls
    shortened_url_code = md5_hash_object.hexdigest()[:8]

    if shortened_url_code not in url_dict:
        url_dict[shortened_url_code] = url_utf8_encoded

    return f"{base_url}/{shortened_url_code}"


def url_shortner_alphanumeric(*, url: str) -> str:
    """
    supports up to 62 ^ 6 urls => 56B urls.
    """
    characters: list[str] = [character for character in string.ascii_letters] + [
        str(number) for number in range(0, 10)
    ]
    url_utf8_encoded = url.encode("utf-8")

    shortened_url_code = ""

    if url_utf8_encoded in url_dict:
        shortened_url_code = url_dict[url_utf8_encoded]
    else:
        shortened_url_code = "".join(random.choice(characters) for _ in range(6))
        url_dict[url_utf8_encoded] = shortened_url_code

    return f"{base_url}/{shortened_url_code}"
