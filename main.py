from functions import url_shortner


def main():
    print("Hello from url-shortner!")
    test_url = "https://www.google.com/search?q=project+bassed+learning+python+url+shortner&sca_esv=c2dc18171226bd7b&sxsrf=AE3TifMunHSGJmPica_IS4klW6UnbMhF-w%3A1757360544127&ei=oDG_aIjCB8GK7M8P9OONoQ0&ved=0ahUKEwiIkuaX9smPAxVBBfsDHfRxI9QQ4dUDCBA&uact=5&oq=project+bassed+learning+python+url+shortner&gs_lp=Egxnd3Mtd2l6LXNlcnAiK3Byb2plY3QgYmFzc2VkIGxlYXJuaW5nIHB5dGhvbiB1cmwgc2hvcnRuZXIyBxAhGKABGAoyBxAhGKABGApI-hJQEFjhEXAAeAKQAQCYAc8CoAHYE6oBBzAuMi41LjO4AQPIAQD4AQGYAgugAokUwgIEEAAYR8ICBxAAGIAEGA3CAgYQABgWGB7CAggQABgIGA0YHsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAgUQABjvBZgDAOIDBRIBMSBAiAYBkAYIkgcHMS4yLjUuM6AHo0CyBwcwLjIuNS4zuAeEFMIHCTAuOC4yLjAuMcgHJg&sclient=gws-wiz-serp"

    print(url_shortner(url=test_url))


if __name__ == "__main__":
    main()
