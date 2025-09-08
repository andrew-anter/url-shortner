import hashlib

url_dict = {}
base_domain = "localhost"
protocol = "http"
base_url = f"{protocol}://{base_domain}"


def main():
    print("Hello from url-shortner!")
    test_url = "https://www.google.com/search?q=project+bassed+learning+python+url+shortner&sca_esv=c2dc18171226bd7b&sxsrf=AE3TifMunHSGJmPica_IS4klW6UnbMhF-w%3A1757360544127&ei=oDG_aIjCB8GK7M8P9OONoQ0&ved=0ahUKEwiIkuaX9smPAxVBBfsDHfRxI9QQ4dUDCBA&uact=5&oq=project+bassed+learning+python+url+shortner&gs_lp=Egxnd3Mtd2l6LXNlcnAiK3Byb2plY3QgYmFzc2VkIGxlYXJuaW5nIHB5dGhvbiB1cmwgc2hvcnRuZXIyBxAhGKABGAoyBxAhGKABGApI-hJQEFjhEXAAeAKQAQCYAc8CoAHYE6oBBzAuMi41LjO4AQPIAQD4AQGYAgugAokUwgIEEAAYR8ICBxAAGIAEGA3CAgYQABgWGB7CAggQABgIGA0YHsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAgUQABjvBZgDAOIDBRIBMSBAiAYBkAYIkgcHMS4yLjUuM6AHo0CyBwcwLjIuNS4zuAeEFMIHCTAuOC4yLjAuMcgHJg&sclient=gws-wiz-serp"

    print(url_shortner(url=test_url))


def url_shortner(*, url: str):
    url_utf8_encoded = url.encode("utf-8")
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(url_utf8_encoded)

    ## will work for 4B urls
    shortened_url_code = md5_hash_object.hexdigest()[:8]

    if shortened_url_code not in url_dict:
        url_dict[shortened_url_code] = url_utf8_encoded
    elif url_dict[shortened_url_code] == url_utf8_encoded:
        return shortened_url_code
    else:
        ## handle collisions
        pass

    return f"{base_url}/{shortened_url_code}"


if __name__ == "__main__":
    main()
