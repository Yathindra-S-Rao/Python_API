import requests

base_url = "https://gorest.co.in/public/v2/users"


def search_by_name(name):
    url = f"{base_url}?name={name}"
    return requests.get(url)


def search_by_id(id):
    url = f"{base_url}?id={id}"
    return requests.get(url)


print(search_by_id("8068000").json())
print(search_by_name("Prof. Vasudha Prajapat").json())

