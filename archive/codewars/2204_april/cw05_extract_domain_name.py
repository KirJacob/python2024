import re


def domain_name(url):
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www", "")
    url = re.search(r'^[^.]*', url).group(0)
    return url