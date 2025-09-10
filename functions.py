import hashlib

url_dict = {}
base_domain = "localhost"
protocol = "http"
base_url = f"{protocol}://{base_domain}"


def url_shortner_md5(*, url: str) -> str:
    url_utf8_encoded = url.encode("utf-8")
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(url_utf8_encoded)

    ## will work for 4B urls
    shortened_url_code = md5_hash_object.hexdigest()[:8]

    if shortened_url_code not in url_dict:
        url_dict[shortened_url_code] = url_utf8_encoded

    return f"{base_url}/{shortened_url_code}"
